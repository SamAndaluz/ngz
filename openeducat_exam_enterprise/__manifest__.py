# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

{
    'name': 'OpenEduCat Exam Enterprise',
    'version': '13.0',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Exam',
    'complexity': "easy",
    'description': """
        This module provide exam management system.
    """,
    'author': 'Tech Receptives',
    'website': 'http://www.openeducat.org',
    'depends': [
        'openeducat_exam',
        'openeducat_core_enterprise',
        'openeducat_student_progress_enterprise',
    ],
    'data': [
        'security/op_security.xml',
        'views/exam_dashboard_view.xml',
        'dashboard/exam_dashboard.xml',
        'wizards/progression_marksheet_wizard_view.xml',
        'views/exam_session_view.xml',
        'views/exam_onbaord.xml',
        'views/openeducat_exam_portal.xml',
        'views/openeducat_marksheet_line_view.xml',
        'views/openeducat_progression_marksheet_line.xml',
        'views/student_progression_exam_portal.xml',
        'reports/exam_progression_report.xml',
    ],
    'demo': [
        'demo/progression_marksheet_demo.xml'
    ],
    'images': [
        'static/description/openeducat_exam_enterprise_banner.jpg',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 75,
    'currency': 'EUR',
    'license': 'OPL-1',
    'live_test_url': 'https://www.openeducat.org/plans'
}
