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


class TimeTablePortal(CustomerPortal):

    @http.route(['/student/timetable/',
                 '/student/timetable/<int:student_id>',
                 '/student/timetable/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_student_timetable_list(self, student_id=None):

        user = request.env.user
        timetable_lst = []
        if student_id:
            student_id = request.env["op.student"].sudo().search(
                [('id', '=', student_id)])
        else:
            student_id = request.env["op.student"].sudo().search(
                [('user_id', '=', user.id)])

        for course_id in student_id.course_detail_ids:
            timetable_id = request.env['op.session'].sudo().search(
                [('course_id', '=', course_id.course_id.id)])
            if timetable_id:
                for rec in timetable_id:
                    timetable_lst.append(rec)

        return request.render(
            "openeducat_timetable_enterprise.openeducat_timetable_portal",
            {'timetable_ids': timetable_lst})
