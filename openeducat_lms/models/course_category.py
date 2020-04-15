# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields


class OpCourseCategory(models.Model):
    _name = "op.course.category"
    _description = "Course Category"

    name = fields.Char('Name', size=32, translate=True, required=True)
    code = fields.Char('Code', required=True)
    desc = fields.Text('Description')
    icon = fields.Char('Icon')
    parent_id = fields.Many2one('op.course.category', 'Parent Category')
    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id)
    active = fields.Boolean(default=True)

    def action_onboarding_course_category_layout(self):
        self.env.user.company_id.onboarding_course_category_layout_state = \
            'done'
