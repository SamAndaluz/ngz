# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

{
    'name': 'Openeducat Lesson Enterprise',
    'version': '13.0',
    'category': 'Education',
    "sequence": 1,
    'summary': 'Manage Lesson Planning',
    'complexity': "easy",
    'author': 'Tech Receptives',
    'website': 'http://www.openeducat.org',
    'depends': [
        'openeducat_timetable',
        'openeducat_parent'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/op_lesson_security.xml',
        'data/ir_sequence.xml',
        'views/lesson_view.xml',
        'menus/openeducat_lesson_menu.xml'
    ],
    'demo': [
        'demo/op_lesson_demo.xml'
    ],
    'images': [
        'static/description/openeducat_lesson_banner.jpg'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 50,
    'currency': 'EUR',
    'license': 'OPL-1',
    'live_test_url': 'https://www.openeducat.org/plans',
}
