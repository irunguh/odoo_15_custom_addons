from odoo import models,api,_,fields
import math, random
class PartnerExtend(models.Model):
    _inherit = 'res.partner'

    def action_approve(self):
        # if this is approved, lets generated client accounts
        # the phone number is used as part of the account details
        bank_account = self.env['account.account'].create({
            'code': self.mobile.replace(" ",""),
            'name': self.name,
            'partner_id': self.id,
            'user_type_id': 1, # Receivable account type in odoo 15
            'reconcile': True
        })
        return self.write({'state': 'approved'})
    def action_decline(self):
        return self.write({'state': 'decline'})
    def action_draft(self):
        return self.write({'state': 'draft'})
    def action_done(self):
        return self.write({'state': 'done'})
    def action_confirm(self):
        return self.write({'state': 'confirm'})
    def action_cancel(self):
        return self.write({'state': 'cancel'})
    # random pins
    def get_random_pin(self):
        # Declare a digits variable
        # which stores all digits
        digits = "0123456789"
        OTP = ""
        # length of password can be chaged
        # by changing value in range
        for i in range(4):
            OTP += digits[math.floor(random.random() * 10)]
        return OTP
    # get logged in user allowed companies
    def get_logged_in_user_allowed_companies(self):
        #self.env.user.company_id.id
        companies = self.env['res.users'].search([('id','=',self.env.user.id)])
        return [('id', 'in', companies.company_ids.ids)]

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('approved', 'Approved'),
        ('decline', 'Declined'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    #customer_account_number = fields.Char(string='Account Number')
    loan_limit = fields.Float(string="Loan Limit", required=False, default=0.00)
    is_insurance = fields.Boolean(string="Is an Insurance",default=False)
    is_enrolled = fields.Boolean(string="Is Enrolled ?", default=False)
    id_type = fields.Selection([('national_id','National Id'),('military_id','Military Id'),
                                ('passport','Passport')],string='Id Type',required=False)
    id_number = fields.Char(string="ID Number",required=False)
    account_pin = fields.Char(string='Account PIN', required=False, default=get_random_pin)
    otp_unsubscribe = fields.Boolean(string='Unsubscribe OTP', default=False)
    registered_via_mobile = fields.Boolean(string='Was Registered via USSD app',
                                           help='Identify all users registered via ussd mobile application', default=False)
    # override the mobile number and make it required
    mobile = fields.Char(string='Mobile Number', help='Enter a valid phone number in the format +2547XXXXXXX',
                         required=True)
    #company_id = fields.Many2one('res.company', 'Company', index=True,default=lambda self: self.env.company,required=True)
    company_id = fields.Many2one('res.company', 'Company',
                                 required=False,domain=get_logged_in_user_allowed_companies)
    is_a_customer = fields.Boolean(string='Is a Customer',default=False)
    decline_customer = fields.Text(string='Decline Customer Reasons')
    business_type = fields.Many2one('business.types',string="Type of Business")
    # we add a constraint to make sure mobile number is unique
    _sql_constraints = [
        ('customer_mobile_unique', 'unique (mobile)',
         'The Customer mobile number must be unique! A customer with similar mobile number exists')
    ]
