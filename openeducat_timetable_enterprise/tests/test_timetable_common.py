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
from odoo.addons.website.tools import MockRequest
from ..controller import onboard
import odoo.tests


class TestTimetableCommon(common.SavepointCase):
    def setUp(self):
        super(TestTimetableCommon, self).setUp()
        self.op_batch = self.env['op.batch']
        self.op_session = self.env['op.session']
        self.op_timing = self.env['op.timing']
        self.op_company = self.env['res.company']


class TimetableControllerTests(TransactionCase):
    def setUp(self):
        super(TimetableControllerTests, self).setUp()
        self.TimetableController = onboard.OnboardingController()


class TestTimetableController(TimetableControllerTests):

    def setUp(self):
        super(TestTimetableController, self).setUp()

    def test_case_timetable_onboarding(self):
        self.TimetableController = onboard.OnboardingController()
        with MockRequest(self.env):
            self.cookies = \
                self.TimetableController.openeducat_timing_onboarding_panel()


@odoo.tests.tagged('post_install', '-at_install')
class TestUi(odoo.tests.HttpCase):

    def test_01_test_student_timetable(self):
        self.start_tour("/", 'test_timetable', login="admin")
