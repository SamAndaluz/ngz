# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################
from odoo.tests import common


class TestLessonCommon(common.SavepointCase):
    def setUp(self):
        super(TestLessonCommon, self).setUp()
        self.op_lesson = self.env['op.lesson']
