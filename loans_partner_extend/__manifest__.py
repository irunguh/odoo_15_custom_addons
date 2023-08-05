# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2021 OTBAfrica <boniface@otbafrica.com>
#
##############################################################################

{
    "name": "Loans Parter Extend",
    'version': '15.0',
    "author": "Amkatek Limited",
    "website": "www.amkatek.com",
    "description": """
     - Add custom features to improve on Customers for Loan Management Application
     - Includes features to register a customer profile and enrolment for loans
    """,

    "category": "Loans",
    "depends": [
        'base','account',
    ],

    "data": [
        'security/ir.model.access.csv',
'wizards/decline_customer.xml',
        'views/partner.xml',
        'views/menus.xml',
        'views/res_users.xml',
        'views/account_account.xml',
        'views/business_types.xml'

    ],
    'application': True,
    "active": False,
    "installable": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
