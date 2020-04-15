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
    'name': 'OpenEduCat Online Tools Base Enterprise',
    'version': '13.0',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Base Module for Manage Online Teaching Tools',
    'complexity': "easy",
    'author': 'Tech Receptives',
    'website': 'http://www.openeducat.org',
    'depends': [
        'calendar',
        'openeducat_core_enterprise',
        'openeducat_timetable_enterprise',
    ],
    'data': [
        'views/timetable_view.xml',
        'views/calender_event.xml',
        'views/online_meeting_portal_view.xml',
    ],
    'images': [
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 50,
    'currency': 'EUR',
    'license': 'OPL-1',
    'live_test_url': 'https://www.openeducat.org/plans'
}
