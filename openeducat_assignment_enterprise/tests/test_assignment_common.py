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

import odoo.tests


class TestAssignmentCommon(common.SavepointCase):
    def setUp(self):
        super(TestAssignmentCommon, self).setUp()
        self.op_assignment_subline = self.env['op.assignment.sub.line']
        self.op_assignment_type = self.env['op.assignment.type']
        self.op_progression_assignment = self.env['op.student.progression']
        self.op_company = self.env['res.company']
        self.op_progression_wizard = self.env['assignment.progress.wizard']


class AssignmentContollerTests(TransactionCase):

    def setUp(self):
        super().setUp()
        self.AssignmentController = onboard.OnboardingController()


class TestAssignmentController(AssignmentContollerTests):

    def setUp(self):
        super(TestAssignmentController, self).setUp()

    def test_case_assignment_onboard(self):
        self.AssignmentController = onboard.OnboardingController()
        with MockRequest(self.env):
            self.cookies = self.AssignmentController. \
                openeducat_assignment_onboarding_panel()


@odoo.tests.tagged('post_install', '-at_install')
class TestUi(odoo.tests.HttpCase):

    def test_01_assignment(self):
        self.start_tour("/", 'test_assignment', login="admin")

    def test_02_assignment_submit(self):
        self.start_tour("/", 'test_assignment_submit', login="admin")
