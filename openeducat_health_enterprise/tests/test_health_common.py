# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo.tests import common


class TestHealthCommon(common.SavepointCase):
    def setUp(self):
        super(TestHealthCommon, self).setUp()
        self.op_health = self.env['op.health']
        self.op_health_line = self.env['op.health.line']
