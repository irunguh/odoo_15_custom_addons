
from odoo import models, fields, api, _
from datetime import datetime

class ClientSessionValues(models.Model):
    _name = 'search.session.values'
    _description = 'Saved session values'

    name = fields.Char(string='Incident')
    session_id = fields.Char(string='Session')
    client_county = fields.Char(string='County')
    image_video = fields.Char(string='Image/Video')
    constituency = fields.Char(string='Constituency')
    polling_stattion = fields.Char(string='Polling Station')
    any_other_details = fields.Char(string='Other Info')
    user = fields.Char(string='Submitted By')
    company_id = fields.Many2one('res.company', 'Company', required=True, index=True,
                                 default=lambda self: self.env.company)