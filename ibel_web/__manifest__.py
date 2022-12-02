# -*- coding: utf-8 -*-
{
    'name': "ibel_web",

    'summary': """
        Customize Ibel backend
        """,
    'description': """
        Customize Ibel backend
    """,

    'author': "Ibel technology",
    'website': "https://ibeltechnology.com.com",
    'license': 'LGPL-3',

    'category': 'Uncategorized',
    'version': '16.0',
    'depends': ['base','base_setup','web'],

 
    "assets": {
        "web.assets_backend": [
            "ibel_web/static/src/js/title.js",
            "ibel_web/static/src/xml/res_config_edition.xml",
        ],
        'web._assets_primary_variables': [
            ('before', 'web/static/src/scss/primary_variables.scss', 'ibel_web/static/src/scss/primary_variables.scss'),
        ],
        'web._assets_secondary_variables': [
            ('before', 'web/static/src/scss/secondary_variables.scss', 'ibel_web/static/src/scss/secondary_variables.scss'),
        ],
    },
   'data': [
        'views/views.xml',
        'views/templates.xml',
        'views/res_config_settings_views.xml',
    ],
    "auto_install": True,
}
