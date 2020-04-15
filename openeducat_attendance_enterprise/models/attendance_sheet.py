# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields


class OpAttendanceSheet(models.Model):
    _inherit = 'op.attendance.sheet'

    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id)

    def action_onboarding_attendance_sheet_layout(self):
        self.env.user.company_id.onboarding_attendance_sheet_layout_state =\
            'done'

    def attendance_sheet_daily(self):
        register_ids = self.env['op.attendance.register'].search(
            [('auto_create', '=', True)])
        for register in register_ids:
            if register.auto_create_type == 'daily':
                self.create({
                    'register_id': register.id,
                    'course_id': register.course_id.id,
                    'batch_id': register.batch_id.id,
                })

    def attendance_sheet_weekly(self):
        register_ids = self.env['op.attendance.register'].search(
            [('auto_create', '=', True)])
        for register in register_ids:
            if register.auto_create_type == 'weekly':
                self.create({
                    'register_id': register.id,
                    'course_id': register.course_id.id,
                    'batch_id': register.batch_id.id,
                })

    def attendance_sheet_monthly(self):
        register_ids = self.env['op.attendance.register'].search(
            [('auto_create', '=', True)])
        for register in register_ids:
            if register.auto_create_type == 'monthly':
                self.create({
                    'register_id': register.id,
                    'course_id': register.course_id.id,
                    'batch_id': register.batch_id.id,
                })

    def new_create_attendance_lines(self, kw=[]):
        sheet_id = kw
        if sheet_id:
            attend_lines = self.env['op.attendance.line'].sudo()
            sheet = self.env['op.attendance.sheet'].sudo().browse(
                sheet_id)
            all_student_search = self.env['op.student'].sudo().search(
                [('course_detail_ids.course_id', '=',
                  sheet.register_id.course_id.id),
                 ('course_detail_ids.batch_id', '=',
                  sheet.register_id.batch_id.id)])
            attendance_lines = attend_lines.search(
                [('attendance_id', '=', sheet.id)])
            students = [record.id for record in all_student_search]
            attendance = [record.student_id.id for record in attendance_lines]
            remaining_students = set(students).difference(attendance)
            for student in remaining_students:
                attend_lines.create({
                    'attendance_id': sheet.id,
                    'student_id': student,
                    'attendance_date': fields.Date.today(),
                    'present': True
                })
        return True
