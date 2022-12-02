# -*- coding: utf-8 -*-
{
    'name': "ibel_pos",

    'summary': """
        Customize Ibel POS
        """,
    'description': """
        Customize Ibel POS
    """,

    'author': "Ibel technology",
    'website': "https://ibeltechnology.com.com",
    'license': 'LGPL-3',

    'category': 'Uncategorized',
    'version': '16.0',
    'depends': ['base','web','point_of_sale'],

    "assets": {
        "point_of_sale.assets": [
            "ibel_pos/static/src/xml/Chrome.xml",
        ],
     },
   'data': [
        'views/templates.xml',
    ],
    "auto_install": True,
}
