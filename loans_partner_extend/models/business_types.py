from odoo import fields,_,api,models

class BusinessTypes(models.Model):
    _name = 'business.types'
    _description='Business Types'

    name = fields.Char(string='Type Name', required=True)
    description = fields.Text(string='Description')
