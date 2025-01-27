# -*- coding: utf-8 -*-
{
    'name': "Birthday",

    'summary': "Automatizacion de correos ",

    'description': "Modulo para automatizar emails a nuestros empleados, para felicitarle su Cumpleaños",

    'author': "Exides",
    'website': "https://www.exides.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/bdayemail.xml',
        'data/cron.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

