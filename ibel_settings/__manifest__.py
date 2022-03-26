# -*- coding: utf-8 -*-

{
    'name': "Ibel settings",
    'version': "14.0",
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
    'qweb': ["static/src/xml/res_config_edition.xml"],
    'license': "AGPL-3",
    'installable': True,
    'application': False,
    'auto_install' : True,
}
