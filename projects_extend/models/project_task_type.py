from odoo import models,api,_,fields
import math, random
class ProjectTaskType(models.Model):

    _inherit = 'project.task.type'

    is_pending = fields.Boolean(string="Is Pending Stage",default=False)
    is_done = fields.Boolean(string="Is Done Stage", default=False)
    company_id = fields.Many2one('res.company', 'Organization', required=True, index=True,
                                 default=lambda self: self.env.company)