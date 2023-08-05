# See LICENSE file for full copyright and licensing details.

{
    "name": "Metabase BI Reports",
    "version": "15.0.1.0.0",
    "author": "Amkatek Limited",
    "category": "Generic Modules/Reports",
    "license": "AGPL-3",
    "summary": "Add menu for reporting module",
    "website": "https://amkatek.com",
    "depends": ["base"],
    "data": [
        "views/dashboard_views.xml",
    ],
    "installable": True,
    "assets": {
        'web.assets_backend': [
            '/metabase_dashboard_views/static/src/css/style.css',
            '/metabase_dashboard_views/static/src/js/manage_reports.js'
        ],
        'web.assets_qweb': [
            'metabase_dashboard_views/static/src/xml/template.xml',
        ]
    }
}
