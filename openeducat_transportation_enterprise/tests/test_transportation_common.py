# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo.tests import common, TransactionCase
from ..controller.onboard import OnboardingController
from odoo.addons.website.tools import MockRequest


class TestTransportationCommon(common.SavepointCase):
    def setUp(self):
        super(TestTransportationCommon, self).setUp()
        self.res_company = self.env['res.company']
        self.op_route = self.env['op.route']
        self.op_route_line = self.env['op.route.line']
        self.op_stop = self.env['op.stop']
        self.op_stop_line = self.env['op.route.stop.line']
        self.op_vehicle = self.env['op.vehicle']


class TransportationCoreroller(TransactionCase):

    def setUp(self):
        super().setUp()


class TestTransportationController(TransportationCoreroller):

    def setUp(self):
        super(TestTransportationController, self).setUp()

    def test_case_1_onboard(self):
        self.onboard_controller = OnboardingController()

        with MockRequest(self.env):
            self.onboard = self.onboard_controller.openeducat_route_onboarding_panel()
