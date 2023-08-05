# -*- coding: utf-8 -*-

from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models, _

selection_level = [('p', 'P'), ('m', 'M'), ('s', 'S')] + [(num, str(num)) for num in range(1, 30)]

#room categories
class PropertyRoomCategories(models.Model):
    _name = 'property.room.categories'
    _description = 'Room Categories'

    name = fields.Char(string='Category Name',required=True)
    description = fields.Text(string='Description')

class PropertyRoom(models.Model):
    _name = 'property.room'
    _description = "Room"
    _inherit = 'property.property'

    name = fields.Char(string="Number")
    building_id = fields.Many2one('property.building', string='Building', required=True)

    level = fields.Selection([('p', 'P'), ('m', 'M'), ('s', 'S'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10')])

    unit_type = fields.Selection([('single_room','Single'),('double_room','Double room'),('1_bedroom','1 Bedroom')
                                  ,('2_bedroom','2 Bedroom'),('3_bedroom','3 Bedroom'),
                                  ('4_bedroom','4 Bedroom'),('shop','Shop'), ('bedsitter','Bedsitter'), ('go_down','GO DOWN')
                                     ,('stall','Stall')
                                  ],string='Unit Type',required=True)

    height = fields.Float()
    perimeter = fields.Float()
    surface_disinsection = fields.Float(string="Area of disinsection", compute="_compute_surface_disinsection", store=True)

    surface = fields.Float("Surface area")
    surface_cleaning_floor = fields.Float(string="Surface cleaning floor")
    surface_cleaning_doors = fields.Float(string="Surface cleaning doors")
    surface_cleaning_windows = fields.Float(string="Surface cleaning window")

    unit_description = fields.Text('Description',required=True,default='Unit Description here, describe features')
    rent_amount = fields.Float(string='Monthly Rent Amount',required=True)
    rent_deposit_months = fields.Integer(string='Number of Months for Deposit',
                                         help='Provide number of Months you require tenants to make deposits for',required=False)
    water_deposit_amount = fields.Float(string='Water Deposit Amount',required=False,default=0.0)
    electricity_deposit_amount = fields.Float(string='Electricity Deposit Amount',required=False,default=0.0)
    ##
    total_initial_pay = fields.Float(string='Total Initial Bill',compute ="_compute_initial_pay",store=False)

    floor_type = fields.Selection([('c', 'Carpet'), ('l', 'Linoleum'), ('w', 'Wood')])

    usage = fields.Selection([
        ('others', 'Others'),
        ('office', 'Office'),
        ('meeting', 'Meeting room'),
        ('kitchens', 'Kitchens'),
        ('laboratory','Laboratory'),
        ('garage','Garage'),
        ('archive', 'Archive'),
        ('warehouse', 'Warehouse'),
        ('log_warehouse', 'Logistics warehouse'),
        ('it_endowments', 'IT endowments (Ranks, Hall Servers)'),
        ('premises', 'Technical premises (thermal, air conditioning, post-transformer)'),
        ('cloakroom', 'Cloakroom'),
        ('sanitary', 'Sanitary group'),
        ('access', 'Access ways'),
        ('lobby', 'Lobby'),
        ('staircase', 'Staircase'),
    ], string="Room/Unit usage", help="The purpose of using the room",required=False,default='others')

    rented_room = fields.Boolean()
    tenant_id = fields.Many2one('res.partner', string="Tenant")

    last_maintenance = fields.Date()
    technical_condition = fields.Selection([('0','Missing'),('1','Unsatisfactory'),('3','good'),('5','very good')],
                                           group_operator='avg')




    #@api.multi
    @api.depends('rent_amount','rent_deposit_months','water_deposit_amount','electricity_deposit_amount')
    def _compute_initial_pay(self):
        #get all totals
        totals = (self.rent_deposit_months * self.rent_amount) + self.electricity_deposit_amount + self.water_deposit_amount + self.rent_amount
        self.total_initial_pay = totals

    #@api.multi
    @api.depends('surface', 'height', 'perimeter')
    def _compute_surface_disinsection(self):
        for room in self:
            room.surface_disinsection = 2 * room.surface + room.height * room.perimeter

    @api.constrains
    def _check_cleaning_surface(self):
        if self.cleaning_surface > self.surface:
            raise ValidationError(_('Cleaning surface most by lower that surface area'))



