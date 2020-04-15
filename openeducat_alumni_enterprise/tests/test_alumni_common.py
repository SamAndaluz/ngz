# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo.tests import common
import odoo.tests


class TestAlumniCommon(common.SavepointCase):
    def setUp(self):
        super(TestAlumniCommon, self).setUp()
        self.op_alumni_group = self.env['op.alumni.group']
        self.op_alumni = self.env['op.student']


@odoo.tests.tagged('post_install', '-at_install')
class TestUi(odoo.tests.HttpCase):

    def test_alumni_group(self):
        self.start_tour("/", 'alumni_group', login="admin")
