from odoo import fields,models,_,api

class ExtendMailTemplate(models.Model):
    _inherit='mail.template'

    description = fields.Text(string="Description")
