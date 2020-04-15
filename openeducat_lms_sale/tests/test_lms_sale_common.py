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


class TestLmsCommonSale(common.SavepointCase):
    def setUp(self):
        super(TestLmsCommonSale, self).setUp()
        self.op_course = self.env['op.course']
        self.op_material = self.env['op.material']
        self.op_enrollment = self.env['op.course.enrollment']
        self.op_sale_order = self.env['sale.order']
