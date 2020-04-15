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


class StudentProgression(CustomerPortal):

    @http.route(['/student/progression/',
                 '/student/progression/<int:student_id>',
                 '/student/progression/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_student_progression(self, student_id=None):

        user = request.env.user
        if user.is_student:
            student_id = request.env['op.student'].sudo().\
                search([('user_id', '=', user.id)])
            progression_id = \
                request.env['op.student.progression'].sudo().search(
                    [('student_id', '=', student_id.id)])
        else:
            progression_id = request.env['op.student.progression'].\
                sudo().search([('student_id', '=', student_id)])

        return request.render(
            "openeducat_student_progress_enterprise."
            "openeducat_student_progression_portal_data",
            {'progression': progression_id})
