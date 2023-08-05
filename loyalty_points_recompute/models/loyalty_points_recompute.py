from odoo import models,fields,_,api
from odoo.exceptions import UserError
import datetime
import re


import logging
_logger = logging.getLogger(__name__)
class loyalty_points_recompute(models.Model):
    _name = 'loyalty.points.recompute'
    _description='Requests to recompute Loyalty points'

    name = fields.Char(string='Reason',states={'draft': [('readonly', False)]},help='Enter Reason for Recomputing points',required=True,readonly=True,)
    date_order = fields.Datetime(string='Request Date', required=True, readonly=True, index=True,
                                 states={'draft': [('readonly', False)]}, copy=False,
                                 default=fields.Datetime.now,
                                 help="Date registered")
    partner_id = fields.Many2one('res.partner',string='Customer',required=True,readonly=True,states={'draft': [('readonly', False)]})
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('approved', 'Approved'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    #
    user_id = fields.Many2one(
        'res.users', string='Created By', index=True, tracking=2, default=lambda self: self.env.user, required=True,readonly=True)

    # approving we re-compute points and set this in customer card
    def action_approve(self):
        # earned points
        browse_points = self.env['loyalty.history'].search([('partner_id','=',self.partner_id.id),('transaction_type','=','receive')])
        customer_points = 0
        for p in browse_points:
            customer_points += p.points
        # lets now set this on customer card
        customer_card_details = self.env['res.partner'].search([('id','=',self.partner_id.id)])
        # now write
        if customer_card_details:
            customer_card_details.write({'loyalty_points': customer_points})
        # mark as approved and done
        return  self.write({'state': 'approved'})

    # confirmation
    def action_confirm(self):
        return  self.write({'state': 'confirm'})
