from odoo import fields,models,_

class ProjectSector(models.Model):
    _name = 'project.sectors'
    _description = 'Project Sectors'

    name = fields.Char(string="Name of Sector",required=True)
    description = fields.Text(string="Description")