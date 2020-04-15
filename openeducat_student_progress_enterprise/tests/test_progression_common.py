# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo.tests import common


class TestProgressionCommon(common.SavepointCase):
    def setUp(self):
        super(TestProgressionCommon, self).setUp()
        self.op_progression = self.env['op.student.progression']
