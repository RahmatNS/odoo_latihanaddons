# -*- coding: utf-8 -*-
{
    'name': "Module ke-2",

    'summary': """Latihan membuat modul Odoo - 2""",

    'description': """
        Setelah membuat membuat module 1, saya membuat module 2
        Module ini juga mengikuti tutorial untuk membuat module open academy
    """,

    'author': "Rahmat Nasution",
    'website': "http://rahmatnasution.xyz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/blog.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}