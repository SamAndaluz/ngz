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
    'name': 'OpenEduCat Alumni Event Enterprise',
    'version': '13.0',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Alumni Event',
    'complexity': "easy",
    'author': 'Tech Receptives',
    'website': 'http://www.openeducat.org',
    'depends': ['base', 'website_event', 'openeducat_alumni_enterprise'],
    'data': ['views/alumni_event_view.xml',
             'views/alumni_event_template_view.xml',
             'views/templates.xml',
             'menus/op_menu.xml'
             ],
    'demo': ['demo/event_event_demo.xml',
             'demo/alumni_event_demo.xml'],
    'images': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 50,
    'currency': 'EUR',
    'license': 'OPL-1',
    'live_test_url': 'https://www.openeducat.org/plans'
}
