# -*- coding: utf-8 -*-
{
    'name': "Module 1 Odoo",

    'summary': """My 1st Odoo Module""",

    'description': """
        Membuat modul dengan Odoo:
            - Kelas Baru
            - Sesi Baru
    """,

    'author': "Rahmat NS",
    'website': "http://rahmatnasution.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_workflow.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}