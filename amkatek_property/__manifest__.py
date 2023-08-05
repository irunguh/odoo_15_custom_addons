# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2008 Deltatech All Rights Reserved
#                    Dorin Hongu <dhongu(@)gmail(.)com , 2020 AmkaTek Limited <amkatekconsulting@gmail.com>
#
##############################################################################

{
    "name": "Kenyan Property Management",
    'version': '15.0.1.0.0',
    "author": "Terrabit, Dorin Hongu, AmkaTek Limited",
    "website": "www.terrabit.ro,www.amkatek.com",
    "description": """
     - Module upgraded to version 15 by AmkaTek (Kenya) Limited. Its customized for Kenyan Market to allows Property Managers easily track 
     rent payments, create bills for there tenants. The app also connects with WhatsApp to allow easily sharing of vacant houses with would be 
     tenants
Functionality:
      - Add, Modify Properties
      - Connects with WhatsApp
      
    """,

    "category": "Property",
    "depends": [
        'mail',
       # 'product'
    ],

    "data": [
        'views/property_menu_view.xml',
        'views/property_config_view.xml',
        'views/property_land_view.xml',
        'views/property_building_view.xml',
        'views/property_room_view.xml',
        'views/property_room_category.xml',
        'views/config_ussd_menus.xml',
        'views/res_partner.xml',
        'views/constituency.xml',
        #'data/data.xml',
        #'data/res.country.state.csv',
         'security/security.xml',
        'security/ir.model.access.csv'

    ],
    'application': True,
    "active": False,
    "installable": True,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
