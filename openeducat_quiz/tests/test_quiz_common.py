# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo.tests import common


class TestQuizCommon(common.SavepointCase):
    def setUp(self):
        super(TestQuizCommon, self).setUp()
        self.op_category = self.env['op.quiz.category']
        self.op_grade = self.env['op.answer.grade']
        self.op_que_bank_type = self.env['op.question.bank.type']
        self.op_que_bank = self.env['op.question.bank']
        self.op_que_bank_line = self.env['op.question.bank.line']
