# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo.tests import common


class TestFacilityCommon(common.SavepointCase):
    def setUp(self):
        super(TestFacilityCommon, self).setUp()
        self.op_facility = self.env['op.facility']
        self.op_facility_line = self.env['op.facility.line']
