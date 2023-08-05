from odoo import models,api,_,fields
import math, random
class ProjectExtend(models.Model):

    _inherit = 'project.project'

    investment_amount = fields.Float(string="Investment Amount",default=0.00)
    no_of_jobs = fields.Integer(string="Jobs",help="No of Jobs to be created")
    days_in_progress = fields.Integer(string="No of Days In Progress",help="No of Days since Start")
    sector = fields.Many2one('project.sectors',string='Sector')
    state_department = fields.Many2one('state.departments',string='State Department')
    government_ministry = fields.Many2one('government.ministry',string='Government Ministry')
    is_a_bill = fields.Boolean(string='Is a Bill',
                               help='This is a bill in parliament?')

    # bill details
    bill_sponsor = fields.Many2one('hr.employee',string='Bill Sponsor')
    date = fields.Date(string='Dated')
    maturity = fields.Date(string='Maturity')
    gazette_no = fields.Integer(string='Gazette No')
    reading_one = fields.Date(string='1st Read')
    reading_two = fields.Date(string='2nd Read')
    reading_three = fields.Date(string='3rd Read')
    remarks = fields.Char(string='Remarks')
    assent = fields.Date(string='Assent')

    #override
    user_id = fields.Many2one('res.users', string='Responsible', default=lambda self: self.env.user, tracking=True)

    company_id = fields.Many2one('res.company', 'Responsible Unit / Ministry', required=True)