# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo.tests import common


class TestAchievementCommon(common.SavepointCase):
    def setUp(self):
        super(TestAchievementCommon, self).setUp()
        self.op_achievement_type = self.env['op.achievement.type']
        self.op_achievement = self.env['op.achievement']
        self.op_progression_achievement = self.env['op.student.progression']
        self.op_progression_wizard = self.env['achievement.progress.wizard']
