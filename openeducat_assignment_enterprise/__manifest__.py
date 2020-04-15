# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

{
    'name': 'OpenEduCat Assignment Enterprise',
    'version': '13.0',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Assgiments',
    'complexity': "easy",
    'author': 'Tech Receptives',
    'website': 'http://www.openeducat.org',
    'depends': [
        'openeducat_assignment',
        'openeducat_core_enterprise',
        'openeducat_student_progress_enterprise',
    ],
    'data': [
        'security/op_security.xml',
        'wizards/progression_assignment_wizard_view.xml',
        'views/openeducat_assignment_portal.xml',
        'views/assignment_view.xml',
        'views/assignment_type_view.xml',
        'views/assignment_sub_line_view.xml',
        'views/assignment_onboard.xml',
        'views/submit_assignment_portal.xml',
        'views/openeducat_assignment_view.xml',
        'views/openeducat_progression_assignment.xml',
        'views/student_progression_assignment_portal.xml',
        'views/assets.xml',
        'reports/assignment_progression_report.xml',
    ],
    'demo': ['demo/progression_assignment_demo.xml'],
    'images': [
        'static/description/openeducat_assignment_enterprise_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 75,
    'currency': 'EUR',
    'license': 'OPL-1',
    'live_test_url': 'https://www.openeducat.org/plans'
}
