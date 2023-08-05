from odoo import models,api,_,fields
import math, random
class ProjectTaskExtend(models.Model):

    _inherit = 'project.task'

    team_leader = fields.Many2one('res.users', string='Team Leader', default=lambda self: self.env.user)
    company_id = fields.Many2one('res.company', 'Organization', required=True, index=True,
                                 default=lambda self: self.env.company)