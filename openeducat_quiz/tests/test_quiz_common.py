# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo.tests import common, TransactionCase
from ..controllers import onboard
from odoo.addons.website.tools import MockRequest
import odoo.tests


class TestQuizCommon(common.SavepointCase):
    def setUp(self):
        super(TestQuizCommon, self).setUp()
        self.op_category = self.env['op.quiz.category']
        self.op_grade = self.env['op.answer.grade']
        self.op_que_bank_type = self.env['op.question.bank.type']
        self.op_que_bank = self.env['op.question.bank']
        self.op_que_bank_line = self.env['op.question.bank.line']
        self.quiz_onboard = self.env['res.company']
        self.op_question_wizard = self.env['op.question.wizard']
        self.op_quiz_result = self.env['op.quiz.result']
        self.op_quiz_result_line = self.env['op.quiz.result.line']
        self.op_quiz = self.env['op.quiz']


class QuizContollerTests(TransactionCase):

    def setUp(self):
        super().setUp()
        self.quizcontroller = onboard.OnboardingController()


class TestQuizController(QuizContollerTests):

    def setUp(self):
        super(TestQuizController, self).setUp()

    def test_quiz_onboard(self):
        with MockRequest(self.env):
            self.onboard = self.quizcontroller.\
                openeducat_quiz_onboarding_panel()


@odoo.tests.tagged('post_install', '-at_install')
class TestUi(odoo.tests.HttpCase):

    def test_01_quiz(self):
        self.start_tour("/", 'quiz_test', login="admin")
