from odoo import fields,models,_

class GovernmentMinistry(models.Model):
    _name = 'government.ministry'
    _description = 'Government Ministry'

    name = fields.Char(string="Name",required=True)
    description = fields.Text(string="Description")
    company_id = fields.Many2one('res.company', 'Government Unit', required=True, index=True,
                                 default=lambda self: self.env.company)
    minister = fields.Many2one('hr.employee',string='Cabinet Secretary',required=True)
    secretary = fields.Many2one('hr.employee',string='Permanent Secretary',required=False)