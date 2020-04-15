# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields


class OpAdmission(models.Model):
    _inherit = 'op.admission'

    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id)


class OpCourse(models.Model):
    _inherit = "op.course"

    admission_count = fields.Integer(
        compute="_compute_admission_count_dashboard_data", string='Admission Count')

    def _compute_admission_count_dashboard_data(self):
        for course in self:
            admission_list = self.env['op.admission'].search_count(
                [('course_id', 'in', [course.id]), ('state', '=', 'done')])
            course.admission_count = admission_list
