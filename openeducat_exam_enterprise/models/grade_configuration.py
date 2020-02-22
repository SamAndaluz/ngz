# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models


class OpGradeConfiguration(models.Model):
    _inherit = "op.grade.configuration"
    _description = "Grade Configuration"

    def action_onboarding_exam_grade_layout(self):
        self.env.user.company_id.onboarding_exam_grade_layout_state = 'done'
