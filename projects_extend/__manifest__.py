# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2021 OTBAfrica <boniface@otbafrica.com>
#
##############################################################################

{
    "name": "Projects Extend",
    'version': '15.0',
    "author": "Amkatek Limited",
    "website": "www.amkatek.com",
    "description": """
     - Add custom features for Project
     - Additional features to support projects in government space
    """,

    "category": "Projects",
    "depends": [
        'base','project','hr'
    ],

    "data": [
        'views/extend_projects.xml',
         'views/state_departments.xml',
        'views/menus.xml',
        'views/project_sectors.xml',
        'views/ministries.xml',
         'security/security.xml',
        'security/ir.model.access.csv'

    ],
    'application': True,
    "active": False,
    "installable": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
