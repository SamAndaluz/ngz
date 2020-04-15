# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo.tests import common, TransactionCase
from ..controllers import onboard, main
from odoo.addons.website.tools import MockRequest


class TestExamCommon(common.SavepointCase):
    def setUp(self):
        super(TestExamCommon, self).setUp()
        self.op_marksheet_line = self.env['op.marksheet.line']
        self.res_company = self.env['res.company']
        self.marksheet_line_progress_wizard = \
            self.env['marksheet.line.progress.wizard']


class ExamContollerTests(TransactionCase):

    def setUp(self):
        super().setUp()
        self.examcontroller = onboard.OnboardingController()


class TestExamController(ExamContollerTests):

    def setUp(self):
        super(TestExamController, self).setUp()

    def test_case_exam_onboard(self):
        self.examcontroller = onboard.OnboardingController()

        with MockRequest(self.env):
            self.onboard = self.examcontroller.\
                openeducat_exam_onboarding_panel()


class TestExamMainController(ExamContollerTests):

    def setUp(self):
        super(TestExamMainController, self).setUp()

    def test_exam_main(self):
        self.exammaincontroller = main.Exam()

        with MockRequest(self.env):
            self.main = self.exammaincontroller.get_exams()
            self.main = self.exammaincontroller.get_exam_chart_details()
            self.main = self.exammaincontroller.get_exam_sessions()
