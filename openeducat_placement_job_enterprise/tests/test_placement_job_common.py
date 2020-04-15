# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo.tests import common


class TestPlacementJobCommon(common.SavepointCase):
    def setUp(self):
        super(TestPlacementJobCommon, self).setUp()
        self.op_activity_announcement = self.env['op.activity.announcement']
        self.op_job_applicant = self.env['op.job.applicant']
