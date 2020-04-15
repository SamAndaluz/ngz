# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields


class OpCourse(models.Model):
    _inherit = "op.course"

    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id)
    color = fields.Integer(string='Color Index', default=0)
    studnet_count = fields.Integer(
        compute="_compute_course_dashboard_data", string='Studnet Count')
    batch_count = fields.Integer(
        compute="_compute_course_dashboard_data", string='Batch Count')
    subject_count = fields.Integer(
        compute="_compute_course_dashboard_data", string='Subject Count')

    def _compute_course_dashboard_data(self):
        for course in self:
            studnet_list = self.env['op.student'].search_count(
                [('course_detail_ids.course_id', 'in', [course.id])])
            batch_list = self.env['op.batch'].search_count(
                [('course_id', 'in', [course.id])])
            subject_list = self.env['op.subject'].search_count(
                [('course_id', 'in', [course.id])])

            course.studnet_count = studnet_list
            course.subject_count = subject_list
            course.batch_count = batch_list

    def action_onboarding_course_layout(self):
        self.env.user.company_id.onboarding_course_layout_state = 'done'
