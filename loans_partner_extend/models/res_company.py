from odoo import fields,models,_,api,Command
import logging
_logger = logging.getLogger(__name__)
# we are going to override the create function and not create a partner everytime we create a company
class ResCompany(models.Model):
    _inherit='res.company'

    # create function override
    @api.model
    def create(self, vals):
        # simply create a company
        company = super(ResCompany, self).create(vals)
        # The write is made on the user to set it automatically in the multi company group.
        self.env.user.write({'company_ids': [Command.link(company.id)]})

        # Make sure that the selected currency is enabled
        if vals.get('currency_id'):
            currency = self.env['res.currency'].browse(vals['currency_id'])
            if not currency.active:
                currency.write({'active': True})
        return company