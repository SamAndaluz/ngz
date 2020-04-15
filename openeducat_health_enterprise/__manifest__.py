# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

{
    'name': 'OpenEduCat Health Enterprise',
    'version': '13.0',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Health',
    'complexity': "easy",
    'author': 'Tech Receptives',
    'website': 'http://www.openeducat.org',
    'depends': [
        'openeducat_core_enterprise'
    ],
    'data': [
        'security/op_security.xml',
        'security/ir.model.access.csv',
        'views/health_view.xml',
        'views/openeducat_health_portal.xml',
        'menus/op_menu.xml',
    ],
    'demo': [
        'demo/health_line_demo.xml',
        'demo/health_demo.xml',
    ],
    'images': [
        'static/description/openeducat_health_enterprise_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 50,
    'currency': 'EUR',
    'license': 'OPL-1',
    'live_test_url': 'https://www.openeducat.org/plans'
}
