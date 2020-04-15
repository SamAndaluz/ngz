# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

{
    'name': 'OpenEduCat CRM Enterprise',
    'version': '13.0',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Convert Lead to Student',
    'complexity': "easy",
    'description': """
        This module provide feature to Convert Lead to Student.

    """,
    'author': 'Tech Receptives',
    'website': 'http://www.openeducat.org',
    'depends': [
        'crm',
        'openeducat_admission_enterprise',
    ],
    'data': ['wizard/crm_lead_to_student.xml',
             'views/crm_lead_view_inherit.xml',
             'views/student_view_inherit.xml'],
    'demo': [],
    'images': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 50,
    'currency': 'EUR',
    'license': 'OPL-1',
}
