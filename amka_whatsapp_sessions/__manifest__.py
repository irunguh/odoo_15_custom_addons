# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------
#
#    Odoo, Amkatek Limited
#    Copyright (C) 2019-Today Amkatek Limited
#    (<https://amkatek.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# ---------------------------------------------------------------------------


{
    'name': 'Amka WhatsApp Session',
    'version': '15.00',
    'author': 'Amkatek',
    'category': 'USSD',
    'website': 'https://amkatek.com',
    'summary': 'Amkatek WhatsApp Session Management' ,
    'description': 'Record WhatsApp sessions and manage whatsapp menus. ',
    'depends': ["sale",'mass_mailing_sms_extend','base'],
    'license': "",
    'demo': [],
    'data': [
        'views/session_view.xml',
        'views/category_view.xml',
        'views/session_submissions.xml',
        'security/ussd_security.xml',
        'security/ir.model.access.csv',
    ],
    'css': [],
    'js': [] ,
    'qweb': ['static/src/xml/*.xml'],
    'images': [],
    'auto_install': False,
    'installable': True
}
