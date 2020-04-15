# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo.http import request, Response

from odoo import http
from odoo.addons.portal.controllers.portal import CustomerPortal


class Exam(http.Controller):

    @http.route("/get_exam_counts", type="json", auth="user")
    def get_exams(self):
        Exam = request.env['op.exam']
        all_exams = Exam.search_count([])
        done_exams = Exam.search_count([('state', '=', 'done')])
        pending_exams = Exam.search_count([('state', '=', 'draft')])
        all_exams_sessions = request.env['op.exam.session'].search_count([])

        return {
            'all_exams': all_exams,
            'pending_exams': pending_exams,
            'done_exams': done_exams,
            'all_exams_sessions': all_exams_sessions
        }

    def get_details(self, domain, subject=False):
        data = []
        for exam in request.env['op.exam'].search(domain):
            pass_count = 0
            res = {}
            for attendant in exam.attendees_line.filtered(
                    lambda att: att.marks >= exam.min_marks):
                pass_count += 1
            lengths = len(exam.attendees_line) if exam.attendees_line else 1
            ratio = (pass_count / lengths) * 100
            if subject:
                res = {
                    'id': exam.id,
                    'name': exam.subject_id.name,
                    'exam': exam.name,
                    'code': exam.exam_code,
                    'start_time': exam.start_time or False,
                    'end_time': exam.end_time or False,
                    'min_marks': exam.min_marks or 0.0,
                    'total_marks': exam.total_marks or 0.0,
                }
            else:
                res = {
                    'name': exam.name,
                    'ratio': ratio
                }
            data.append(res)
        return data

    @http.route("/get_exam_chart_details", type="json", auth="user")
    def get_exam_chart_details(self):
        return self.get_details([('attendees_line', '!=', False)])

    @http.route("/get_subject_details", type="json", auth="user")
    def get_subject_details(self, session_id):
        return self.get_details([
            ('session_id', '=', int(session_id))], subject=True)

    @http.route("/get_exam_sessions", type="json", auth="user")
    def get_exam_sessions(self):
        return {
            'session_ids': request.env['op.exam.session'].search_read(
                [], ['id', 'name'])
        }


class ExamPortal(CustomerPortal):

    @http.route(['/student/exam/',
                 '/student/exam/<int:student_id>',
                 '/student/exam/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_student_exam_list(self, student_id=None):

        user = request.env.user
        if user.is_student:
            student_id = request.env["op.student"].sudo().search(
                [('user_id', '=', user.id)])
            exam_id = request.env['op.marksheet.line'].sudo().search(
                [('student_id', '=', student_id.id)])
        else:
            exam_id = request.env['op.marksheet.line'].sudo().search(
                [('student_id', '=', student_id)])

        return request.render(
            "openeducat_exam_enterprise.openeducat_exam_portal",
            {'exam_ids': exam_id})

    def check_exam_access(self, exam_id=None):

        marksheet_id = request.env['op.marksheet.line'].sudo().search(
            [('id', '=', exam_id)])
        user = request.env.user
        user_list = []
        count = 0
        for rec in marksheet_id.student_id:
            if rec.user_id:
                user_list.append(rec.user_id)

        if user.partner_id.is_parent:
            parent_id = request.env['op.parent'].sudo().search(
                [('name', '=', user.partner_id.id)])
            for student_id in parent_id.student_ids:
                if student_id.partner_id.user_id in user_list:
                    count += 1
            if count > 0:
                return True
            else:
                return False
        else:
            if user not in user_list:
                return False
            else:
                return True

    @http.route(['/student/exam/data/<int:exam_id>'],
                type='http', auth="user", website=True)
    def portal_student_exam_form(self, exam_id):

        exam_instance = request.env['op.marksheet.line'].sudo().search(
            [('id', '=', exam_id)])
        access_role = self.check_exam_access(exam_instance.id)
        if access_role is False:
            return Response("[Bad Request]", status=404)

        return request.render(
            "openeducat_exam_enterprise.openeducat_exam_portal_data",
            {'exam_ids': exam_instance})
