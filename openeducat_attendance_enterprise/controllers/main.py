# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo.http import request

from odoo import http
from odoo.addons.portal.controllers.portal import CustomerPortal


class AttendancePortal(CustomerPortal):

    @http.route(['/student/attendance/',
                 '/student/attendance/<int:student_id>',
                 '/student/attendance/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_student_attendance_list(self, student_id=None):

        user = request.env.user
        if user.is_student:
            student_id = request.env["op.student"].sudo().search(
                [('user_id', '=', user.id)])
            attendance_id = request.env['op.attendance.line'].sudo().search(
                [('student_id', '=', student_id.id)])
        else:
            attendance_id = request.env['op.attendance.line'].sudo().search(
                [('student_id', '=', student_id)])

        return request.render(
            "openeducat_attendance_enterprise.openeducat_attendance_portal",
            {'attendance_ids': attendance_id})
