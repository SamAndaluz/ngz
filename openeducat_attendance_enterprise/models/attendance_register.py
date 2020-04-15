# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields


class OpAttendanceRegister(models.Model):
    _inherit = "op.attendance.register"

    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id)
    auto_create = fields.Boolean('Auto Create')
    auto_create_type = fields.Selection([
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly')], 'Auto create sheet duration')

    def action_onboarding_attendance_register_layout(self):
        self.env.user.company_id.onboarding_attendance_register_layout_state =\
            'done'
