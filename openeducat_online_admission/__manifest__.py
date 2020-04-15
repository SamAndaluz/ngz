# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

{
    'name': 'OpenEduCat Online Admission',
    'version': '13.0',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Online Admission',
    'complexity': "easy",
    'author': 'Tech Receptives',
    'website': 'http://www.openeducat.org',
    'depends': [
        'website_sale',
        'website_payment',
        'openeducat_admission',
        'openeducat_core_enterprise'
    ],
    'data': [
        'views/assets.xml',
        'views/admission_view.xml',
        'views/course_view.xml',
        'views/admission_website_view.xml',
        'views/student_registration_details_portal.xml',
    ],
    'images': [
        'static/description/openeducat_online_admission_banner.jpg',
    ],
    'demo': ['demo/product_demo.xml',
             'demo/op_course_demo.xml',
             'demo/admission_register_demo.xml'],
    'css': [],
    'qweb': [],
    'js': [
        'static/src/js/custome.js'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 125,
    'currency': 'EUR',
    'license': 'OPL-1',
    'live_test_url': 'https://www.openeducat.org/plans'
}
