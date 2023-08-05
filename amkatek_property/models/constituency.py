
from odoo import models, fields, api, _
from datetime import datetime

class constituency(models.Model):
    _name = 'voter.constituency'
    _description = 'Voter Constituency'

    name = fields.Char(string='Name')
    county_id = fields.Many2one('property.region',string='County')