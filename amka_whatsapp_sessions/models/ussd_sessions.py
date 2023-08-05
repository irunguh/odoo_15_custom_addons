from odoo import models,api,fields,_
from odoo.exceptions import ValidationError, Warning,UserError
import time
import datetime
import logging

_logger = logging.getLogger(__name__)



class USSDSession(models.Model):
    _name = 'ussd.session'
    _description = 'USSD Session Management'

    name = fields.Char('Customer Name',required=False, size=256,help='Enter a valid Customer Name')
    phone_no = fields.Char('Phone Number', required=True, size=256, help='Customer Phone')
    session_id = fields.Char('Session Id',required=True,help='Session Identity',size=256)
    level = fields.Integer('Level',required=True,help='Level')
    email = fields.Char('Email',required=False,size=256,help='Client Email Address')
    lang = fields.Char('User Language',required=False,size=256,default='en',help="User Preferred language")
    unique_session_id = fields.Char(string="Unique UUID")
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True,
                                 default=lambda self: self.env.company)
    customer_id = fields.Char(string="ID")
    pin = fields.Char(string="PIN")
    related_partner_record = fields.Many2one('res.partner',string="Related Partner")
    # @api.model
    # def create(self, vals):
    #     # create ussd record
    #     create_id = super(USSDSession, self).create(vals)
    #     _logger.info("Session created {0}".format(create_id))
    #     if create_id:
    #         # once the user is created in db, create user in res.partner model
    #
    #         client_name = vals.get('phone_no')
    #         client_phone = vals.get('phone_no')
    #         client_email = vals.get('placeholder@youremail.com')
    #         # partner details setup
    #         partner_info = [{'name': client_name, 'email': client_email, 'phone': client_phone}]
    #         # create respective partner record
    #         res_partner_object = self.env['res.partner'].sudo().create(partner_info)
    #         #partner = res_partner_object.create(partner_info)
    #


    #override write function
    def write(self, vals):
        result = super(USSDSession, self).write(vals)
        #print "Values to write {0}".format(vals)
        #print "Current record id {0}".format(self.id)
        #search current record phone number
        #search_res = self.search(limit=1)
        #print "Search  current record {0}".format(search_res)
        recs = self.browse(self.id)
        #print "Current record browse {0}".format(recs)
        read = self.read({'phone_no','name','email'})
        #print "Read {0}".format(read[0])
        #print "Details {0}".format(read)
        phone_no = None
        email = None
        name = None
        for item in read:
            phone_no = item['phone_no']
            email = item['email']
            name = item['name']
        #sync res partner record
        #res_partner_obj = self.pool.get('res.partner')
        res_partner_obj_ids = self.env['res.partner'].browse()
        partner_record = res_partner_obj_ids.search([('phone','=',phone_no)],limit=1)
        #
        if partner_record:
           update_vals = {'name' : name, 'email': email, 'phone':phone_no}
           #sync partner record
           partner_record.write(update_vals)

        return result
