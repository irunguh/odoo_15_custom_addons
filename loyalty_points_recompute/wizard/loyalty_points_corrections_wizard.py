from odoo import api, fields, models,_
from odoo.exceptions import AccessError, UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)
from datetime import datetime
class LoyaltyRecomputeWizard(models.TransientModel):
    _name = 'loyalty.points.recompute_wizard'

    customer_id = fields.Many2one('res.partner',string='Customer',required=True)

    def get_points_from_pricelist(self, pricelist_id, product_id):
        # print("Debug::::: Search using {0} {1}".format(pricelist_id,product_id))
        _logger.info("Debug:::: get_points_from_pricelist{0} ::: product_id {1} ".format(pricelist_id, product_id))
        # using pricelist id, and product id get a specific product set points
        set_points = self.env['product.pricelist.item'].search(
            [('pricelist_id', '=', pricelist_id), ('product_tmpl_id', '=', product_id)], limit=1)

        return int(set_points.ice_points_to_accrue)
    def recompute_points_for_customers(self):
        # TODO -

        # customer pricelist
        point_cal = int(self.env['ir.config_parameter'].sudo().get_param('bi_sale_loyalty.point_cal'))

        loyalty_history = False
        if point_cal > 0:
            # customer_pricelist_id = invoice.partner_id.property_product_pricelist.id
            ########## invoice lines
            # We correct for a customer
            # first lets cancel all points entries that had created for this customer
            customer_existing_points = self.env['loyalty.history'].search([('partner_id','=',self.customer_id.id)])
            if customer_existing_points:
                for p in customer_existing_points:
                    p.write({'transaction_type': 'cancel', 'extra_note': 'Cancelled for Points correction'})
            invoices = self.env['account.move'].search(
                [('invoice_payment_state', '=', 'paid'), ('type', '=', 'out_invoice'),('partner_id','=',self.customer_id.id)])
            for inv in invoices:
                read_invoice_lines = self.env['account.move.line'].search([('move_id', '=', inv.id),
                                                                           ('parent_state', '=', 'posted'),
                                                                           ('product_id', '!=', False)])
                custom_points = 0
                # loop
                for lines in read_invoice_lines:
                    # this is an invoice for buying ice points
                    if lines.product_id.is_for_ice_points == True:
                        # 1 point = 2
                        total_paid = (lines.quantity * lines.product_id.list_price)
                        results = (total_paid * point_cal)
                        # custom_points += results/lines.product_id.list_price
                        custom_points += lines.quantity
                    else:  # Award as set per price
                        custom_points += self.get_points_from_pricelist(inv.partner_id.property_product_pricelist.id,
                                                                        lines.product_id.id) * lines.quantity

                # this is a summation of points set on a product and quntity purchased
                new_loyalty = int(custom_points)
                # print("************** POINTS ********************")
                # print(new_loyalty)
                ########## end custom
                if new_loyalty > 0:
                    # if this an invoice we sent to customer not supplier invoice
                    if inv.type == 'out_invoice':
                        # get payment reference linked to this invoice
                        payment_ref_obj = self.env['account.payment'].search([('communication', '=', inv.name)])
                        # multiple invoices reconciled manually
                        # use extra note field to show invoice
                        extra_note = ''
                        if not payment_ref_obj:
                            # try to search for invoices with this as payment reference
                            # payment_ref_obj = self.env['account.payment'].search([('move_name','in',self.ids)])
                            # TODO - figure out how the relationship on reconcilation payment is created
                            # TODO - we have a situation where a user manually reconciles check payments which can link to multiple invoices and searching to link and show payment reference in loyalty points is impossible
                            extra_note = inv.name  # we just note the connected invoice

                        vals = {
                            'transaction_type': 'receive',
                            'total_payment_amount': inv.partner_id.total_amount + inv.amount_total,
                            # 'total_points': inv.partner_id.loyalty_points + new_loyalty,
                            'payment_id': payment_ref_obj.id,
                            'partner_id': inv.partner_id.id,
                            'date': datetime.now().date(),
                            'points': new_loyalty,
                            'payment_amount': inv.amount_total,
                            'extra_note': extra_note
                        }
                        # check invoice is paid
                        # we only assign points if its fully paid
                        if inv.invoice_payment_state == 'paid':
                            _logger.info("Debug::::::::Recompute and add points {0} To {1}".format(new_loyalty,inv.partner_id.name))
                            # _logger.info("XXXXXXXXXXX We have disabled notifications for now !!!!")
                            loyalty_history = self.env['loyalty.history'].create(vals)