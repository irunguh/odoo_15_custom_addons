from odoo import fields,models,_

class StateDepartments(models.Model):
    _name = 'state.departments'
    _description = 'State Departments'

    name = fields.Char(string="Name",required=True)
    description = fields.Text(string="Description")
    company_id = fields.Many2one('res.company', 'Government Unit', required=False, index=True,
                                 default=lambda self: self.env.company)
    department_head = fields.Many2one('hr.employee',string='Principal Secretary',required=True)
    ministry = fields.Many2one('government.ministry',string='Ministry',required=True)