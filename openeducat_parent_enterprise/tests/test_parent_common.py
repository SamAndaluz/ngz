# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo.tests import common, TransactionCase
from ..controller import onboard
from odoo.addons.website.tools import MockRequest


class TestParentCommon(common.SavepointCase):
    def setUp(self):
        super(TestParentCommon, self).setUp()
        self.op_parent = self.env['op.parent']
        self.res_company = self.env['res.company']


class ParentController(TransactionCase):

    def setUp(self):
        super().setUp()


class TestParentController(ParentController):

    def setUp(self):
        super(TestParentController, self).setUp()

    def test_case_1_onboard(self):
        self.parent_onboard_controller = onboard.OnboardingController()

        with MockRequest(self.env):
            self.parent_onboard = self.parent_onboard_controller. \
                openeducat_parent_onboarding_panel()
