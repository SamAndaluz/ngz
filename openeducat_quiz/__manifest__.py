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
    'name': 'OpenEduCat Quiz Management',
    'version': '13.0',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Quiz Management',
    'complexity': "easy",
    'author': 'Tech Receptives',
    'website': 'http://www.openeducat.org',
    'depends': [
        'base',
        'portal',
        'gamification',
        'openeducat_web',
    ],
    'data': [
        'security/op_security.xml',
        'security/ir.model.access.csv',
        'views/category_view.xml',
        'wizard/question_view.xml',
        'wizard/update_mark_view.xml',
        'data/portal_result_sequence.xml',
        'views/quiz_view.xml',
        'views/result_view.xml',
        'views/website_view.xml',
        'views/website_view_fullscreen.xml',
        'views/quiz_asset.xml',
        'views/question_bank_view.xml',
        'views/quiz_embeded.xml',
        'views/my_account_result.xml',
        'views/onboard.xml',
        'menus/op_menu.xml',

    ],
    'demo': [
        'demo/question_bank_type.xml',
        'demo/answer_grade.xml',
        'demo/question_bank.xml',
        'demo/question_bank_math.xml',
        'demo/question_bank_gk.xml',
        'demo/question_bank_c.xml',
        'demo/question_bank_cpp.xml',
        'demo/question_bank_science.xml',
        'demo/question_bank_reference_gk.xml',
        'demo/op_quiz_category_data.xml',
        'demo/op_quiz_data.xml',
        'demo/op_quiz_line_data.xml',
        'demo/op_quiz_result_line.xml',
        'demo/op_quiz_result.xml',

    ],
    'images': [
        'static/description/openeducat_quiz_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 100,
    'currency': 'EUR',
    'license': 'OPL-1',
    'live_test_url': 'https://www.openeducat.org/plans'
}
