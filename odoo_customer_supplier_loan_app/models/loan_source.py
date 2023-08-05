from odoo import api, fields, models, _

class LoanSource(models.Model):
    _name='loan.source'
    _description='Loan Source'

    name = fields.Char(string='Name',required=True)
    description = fields.Text(string='Description')
    company_id = fields.Many2one('res.company', default=lambda self: self.env.user.company_id.id,
                                 string="Company", required=True)