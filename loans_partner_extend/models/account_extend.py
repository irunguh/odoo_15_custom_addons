from odoo import models,api,_,fields

class AccountExtend(models.Model):
    _inherit='account.account'

    partner_id = fields.Many2one('res.partner',string='Customer')