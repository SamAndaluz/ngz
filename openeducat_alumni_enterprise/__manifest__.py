# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

{
    'name': 'OpenEduCat Alumni Enterprise',
    'version': '13.0',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Alumni',
    'complexity': "easy",
    'author': 'Tech Receptives',
    'website': 'http://www.openeducat.org',
    'depends': ['base', 'openeducat_core_enterprise', 'website_profile',
                'website_forum', 'product', 'account'],
    'data': [
        'security/op_security.xml',
        'security/ir.model.access.csv',
        'views/alumni_view.xml',
        'views/alumni_group_view.xml',
        'views/web_alumni_view.xml',
        'views/student_template_view.xml',
        'views/templates.xml',
        'menus/op_menu.xml'],
    'demo': [
        'demo/product_demo.xml',
        'demo/student_demo.xml',
        'demo/alumni_group_demo.xml'
    ],
    'images': [
        'static/description/openeducat_alumni_enterprise_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 50,
    'currency': 'EUR',
    'license': 'OPL-1',
    'live_test_url': 'https://www.openeducat.org/plans'
}
