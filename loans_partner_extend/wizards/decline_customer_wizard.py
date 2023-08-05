from odoo import fields,_,models,api

class DeclineCustomerWizard(models.TransientModel):
    _name='decline.customer.wizard'

    name = fields.Text(string='Decline Reasons',required=True)


    def decline_and_notify(self):
        customer = self.env['res.partner'].browse(self._context.get('active_ids', []))
        if customer:
           customer.update({"state": "decline","decline_customer": self.name})