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


class TestFeesCommon(common.SavepointCase):
    def setUp(self):
        super(TestFeesCommon, self).setUp()
        self.op_fees_template = self.env['op.fees.template.line']
        self.op_fees_term_line = self.env['op.fees.terms.line']
        self.op_fees_term = self.env['op.fees.terms']
