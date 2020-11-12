# -*- coding: utf-8 -*-
{
    'name': "hr_expense_extended",

    'summary': """
        This module extends hr_expense functionality.""",

    'description': """
        This module extends hr_expense functionality.
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_expense'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/settings.xml',
        'views/hr_expense.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
