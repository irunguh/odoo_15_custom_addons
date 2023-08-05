from odoo import models,api,fields,_
from odoo.exceptions import ValidationError, Warning,UserError
import time
import datetime


class USSDServiceCategory(models.Model):
    _name = 'ussd.service.category'
    _description = 'USSD Service Category'

    name = fields.Char("Session Id",size=256,required=True,help="Session Id from your service provider")
    categ_id = fields.Integer("Category", required=True, help="Current selected category")
    user_id = fields.Char("Phone Number",size=256,required=True,help="Client phone number used to identify the user")
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True,
                                 default=lambda self: self.env.company)

