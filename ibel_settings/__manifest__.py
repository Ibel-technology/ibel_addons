# -*- coding: utf-8 -*-

{
    'name': "Ibel settings",
    'version': "16.0",
    'summary': """Debrand Odoo settings views""",
    'description': """Debrand Odoo settings views""",
    'author': "Ibel technology",
    'company': "Ibel technology",
    'maintainer': "Ibel technology",
    'website': "https://ibeltechnology.com/",
    'category': 'Tools',
    'depends': ['base_setup',],
    'data': [
        'views/res_config_settings_views.xml',
    ],

    'license': "AGPL-3",
    'installable': True,
    'application': False,
    "assets": {
        "web.assets_backend": [
            "ibel_settings/static/src/xml/res_config_edition.xml",
        ],
     },
    'auto_install' : True,
}
