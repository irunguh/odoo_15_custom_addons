# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2021 AmkaTek Limited <amkatekconsulting@gmail.com>
#
##############################################################################

{
    "name": "Re-compute Customer Points",
    'version': '13.0',
    "author": "AmkaTek Limited",
    "website": "www.amkatek.com",
    "description": """
     - Modules Re-computes a customer loyalty points. This come in hardy for issues with Customer Points
    """,

    "category": "Sales",
    "depends": [
        'bi_sale_loyalty'
    ],

    "data": [
        'views/loyalty_points_recompute.xml',
        'wizard/loyalty_points_correction_wizard.xml',
        'security/security.xml',
        'security/ir.model.access.csv'
    ],
    'application': True,
    "active": False,
    "installable": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
