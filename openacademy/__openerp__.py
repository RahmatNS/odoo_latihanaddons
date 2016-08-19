# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Module ke-3 Oleh Rahmat NS""",

    'description': """
        Sebelumnya sudah dibangun dua modul:
            - Module 1
            - Module 2
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
        'templates.xml',
        'views/openacademy.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}