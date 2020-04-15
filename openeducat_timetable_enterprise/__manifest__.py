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
    'name': 'OpenEduCat Timetable Enterprise',
    'version': '13.0',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage TimeTables',
    'complexity': "easy",
    'author': 'Tech Receptives',
    'website': 'http://www.openeducat.org',
    'depends': [
        'openeducat_timetable',
        'openeducat_core_enterprise'
    ],
    'data': [
        'security/op_security.xml',
        'views/templates.xml',
        'views/timetable_view.xml',
        'views/timing_view.xml',
        'views/openeducat_dashboard_view.xml',
        'views/timetable_onboard.xml',
        'views/openeducat_timetable_portal.xml',
    ],
    'demo': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': [
        'static/description/openeducat_timetable_enterprise_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 75,
    'currency': 'EUR',
    'license': 'OPL-1',
    'live_test_url': 'https://www.openeducat.org/plans'
}
