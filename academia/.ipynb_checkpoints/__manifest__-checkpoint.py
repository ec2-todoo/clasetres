# -*- coding: utf-8 -*-
{
    'name': "academia",

    'summary': """
        Descripcion corta""",

    'description': """
        Descripcion larga
    """,

    'author': "Todoo SAS",
    'website': "http://www.todoo.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Academico',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['contacts','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/vista_academia.xml',
        'views/vista_res_partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
