from odoo import models,api,_,fields
#room categories
class PropertyUSSDMenus(models.Model):
    _name = 'property.ussd.menus'
    _description = 'Property USSD Menus'

    name = fields.Char(string='Menu Name',required=True)
    description = fields.Text(string='Description')