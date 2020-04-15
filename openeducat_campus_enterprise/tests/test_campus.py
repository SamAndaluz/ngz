# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################
from .test_campus_common import TestCampusCommon


class TestCampusOnboard(TestCampusCommon):

    def setUp(self):
        super(TestCampusOnboard, self).setUp()

    def test_campus_onboard(self):
        onboard = self.campus_onboard.search([])
        onboard.action_close_campus_panel_onboarding()
        onboard.action_onboarding_facilities_layout()
        onboard.action_done_onboarding_facilities_layout()
        onboard.action_onboarding_facilities_type_layout()


class TestCampusFacility(TestCampusCommon):

    def setUp(self):
        super(TestCampusFacility, self).setUp()

    def test_campus_facility(self):
        facility = self.op_campus_facility.search([])
        facility.name_get()
        facility.action_onboarding_facilities_layout()
