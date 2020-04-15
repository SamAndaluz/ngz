# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################
from .test_exam_common import TestExamCommon


class TestMarksheetLine(TestExamCommon):

    def setUp(self):
        super(TestMarksheetLine, self).setUp()

    def test_marksheet_line(self):
        line = self.op_marksheet_line.search([])
        for x in line:
            x.onchange_student_marksheet_line_progrssion()


class TestResCompany(TestExamCommon):

    def setUp(self):
        super(TestResCompany, self).setUp()

    def test_res_company(self):
        company = self.res_company.search([])

        company.action_close_exam_panel_onboarding()
        company.action_onboarding_exam_layout()
        company.action_onboarding_exam_room_layout()
        company.action_onboarding_exam_grade_layout()
        company.update_exam_onboarding_state()
