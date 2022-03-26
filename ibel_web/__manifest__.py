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

    'category': 'Uncategorized',
    'version': '14.0',
    'depends': ['base', 'web'],

    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    
    'qweb': ["static/src/xml/res_config_edition.xml"],
    "auto_install": True,
}
