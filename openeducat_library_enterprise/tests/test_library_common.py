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
from ..controllers import onboard, main
import odoo.tests


class TestLibraryCommon(common.SavepointCase):
    def setUp(self):
        super(TestLibraryCommon, self).setUp()
        self.op_media_type = self.env['op.media.type']
        self.op_media_queue = self.env['op.media.queue']
        self.op_media_movement = self.env['op.media.movement']
        self.op_media = self.env['op.media']
        self.op_media_publisher = self.env['op.publisher']
        self.op_library_card = self.env['op.library.card']
        self.op_library_card_type = self.env['op.library.card.type']
        self.op_media_author = self.env['op.author']
        self.op_company = self.env['res.company']
        self.barcode_issue_media = self.env['barcode.issue.media']


class LibraryControllerTests(TransactionCase):
    def setUp(self):
        super(LibraryControllerTests, self).setUp()
        self.LibraryController = onboard.OnboardingController()


class TestLibraryController(LibraryControllerTests):

    def setUp(self):
        super(TestLibraryController, self).setUp()

    def test_case_library_onboarding(self):
        self.LibraryController = onboard.OnboardingController()
        with MockRequest(self.env):
            self.cookies = \
                self.LibraryController.openeducat_library_onboarding_panel()


class LibraryDashboardControllerTests(TransactionCase):
    def setUp(self):
        super(LibraryDashboardControllerTests, self).setUp()
        self.DashboardController = main.OpenEduCatLibraryController()


class TestLibraryDashboardController(LibraryDashboardControllerTests):

    def setUp(self):
        super(TestLibraryDashboardController, self).setUp()

    def test_case_library_dashboard(self):
        self.DashboardController = main.OpenEduCatLibraryController()
        with MockRequest(self.env):
            self.cookies = \
                self.DashboardController.compute_library_dashboard_data()


@odoo.tests.tagged('post_install', '-at_install')
class TestUi(odoo.tests.HttpCase):

    def test_01_admin_checkout(self):
        self.start_tour("/", 'test_library_media', login="admin")

    def test_02_admin_checkout(self):
        self.start_tour("/", 'test_library', login="admin")

    def test_03_admin_checkout(self):
        self.start_tour("/", 'test_media_queue_request', login="admin")
