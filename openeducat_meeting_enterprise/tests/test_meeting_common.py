# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo.tests import common, TransactionCase
from odoo.addons.website.tools import MockRequest
from ..controller import onboard


class TestMeetingCommon(common.SavepointCase):
    def setUp(self):
        super(TestMeetingCommon, self).setUp()
        self.op_meeting = self.env['op.meeting']


class MeetingContollerTests(TransactionCase):

    def setUp(self):
        super().setUp()
        self.MeetingContollerTests = onboard.OnboardingController()


class TestMeetingController(MeetingContollerTests):

    def setUp(self):
        super(TestMeetingController, self).setUp()

    def test_case_meeting_onboard(self):
        self.MeetingContollerTests = onboard.OnboardingController()
        with MockRequest(self.env):
            self.cookies = self.MeetingContollerTests. \
                openeducat_meeting_onboarding_panel()
