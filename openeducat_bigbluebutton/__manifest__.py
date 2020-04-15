# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

{
    'name': 'OpenEduCat Bigbluebutton Integration',
    'version': '13.0',
    'category': 'Education',
    "sequence": 3,
    'summary': 'BigBlueButton',
    'complexity': "easy",
    'author': 'Tech Receptives',
    'website': 'http://www.openeducat.org',
    'depends': [
        'openeducat_web',
        'openeducat_online_tools_enterprise',
    ],
    'data': [

        "data/parameter_data.xml",
        "wizard/meeting_view.xml",
        "views/online_meeting_timetable_template.xml",
        "views/res_config_setting_view.xml",
        "views/calender_event.xml",
    ],
    'images': [
        'static/description/openeducat_bigbluebutton_banner.jpg',
    ],
    'demo': [],
    'css': [],
    'qweb': [],
    'js': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 75,
    'currency': 'EUR',
    'license': 'OPL-1',
    'external_dependencies': {'python': ['xmltodict']},
    'live_test_url': 'https://www.openeducat.org/plans'
}
