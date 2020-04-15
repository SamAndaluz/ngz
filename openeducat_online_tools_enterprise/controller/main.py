# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################


from odoo.http import request, Response

from odoo import http
from odoo.addons.portal.controllers.portal import CustomerPortal


class OnlineMeetingPortal(CustomerPortal):

    def check_online_meeting_access(self, meeting_id=None):

        meeting_id = request.env['calendar.event'].sudo().search(
            [('id', '=', meeting_id), ('online_meeting', '=', True)])
        user = request.env.user
        user_list = []
        count = 0
        for rec in meeting_id:
            if rec.partner_ids:
                for partner in rec.partner_ids:
                    user_list.append(partner.id)
        if user.partner_id.is_parent:
            parent_id = request.env['op.parent'].sudo().search(
                [('name', '=', user.partner_id.id)])
            for student_id in parent_id.student_ids:
                if student_id.partner_id.id in user_list:
                    count += 1
            if count > 0:
                return True
            else:
                return False
        else:
            if user.partner_id.id not in user_list:
                return False
            else:
                return True

    @http.route(['/online/meeting/',
                 '/online/meeting/<int:student_id>',
                 '/online/meeting/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_online_meeting_list(self, student_id=None, **kw):
        user = request.env.user
        online_meeting_id = request.env["calendar.event"].sudo().search([
            ('partner_ids', '=', user.partner_id.id),
            ('online_meeting', '=', True)])

        if user.partner_id.is_parent:
            parent_id = request.env['op.parent'].sudo().search(
                [('name', '=', user.partner_id.id)])
            studnet_list = [rec.id for rec in parent_id.student_ids]

            if student_id in studnet_list:
                student_id = request.env['op.student'].sudo().search(
                    [('id', '=', student_id)])
                online_meeting_id = request.env["calendar.event"].sudo().search(
                    [('partner_ids', '=', student_id.partner_id.id),
                     ('online_meeting', '=', True)])

        return request.render(
            "openeducat_online_tools_enterprise.openeducat_online_meeting_portal",
            {'meeting_ids': online_meeting_id})

    @http.route(['/online/meeting/information/<int:meeting_id>', ],
                type='http', auth="user", website=True)
    def portal_online_meeting_form(self, meeting_id, **kw):

        user = request.env.user
        online_meeting_id = request.env['calendar.event'].sudo().search(
            [('id', '=', meeting_id)])

        attendee = []
        for record in online_meeting_id.attendee_ids:
            if user.partner_id.is_parent:
                parent_id = request.env['op.parent'].sudo().search(
                    [('name', '=', user.partner_id.id)])
                for rec in parent_id.student_ids:
                    if rec.partner_id.id == record.partner_id.id:
                        attendee.append({
                            'email': record.email,
                            'url': record.attendee_meeting_url,
                            'apw': record.apw
                        })
            if user.partner_id.id == record.partner_id.id:
                attendee.append({
                    'email': record.email,
                    'url': record.attendee_meeting_url,
                    'apw': record.apw
                })

        res = self.check_online_meeting_access(online_meeting_id.id)
        if res is False:
            return Response("[Bad Request]", status=404)

        return request.render(
            "openeducat_online_tools_enterprise.openeducat_online_meeting_portal_data",
            {'meeting_ids': online_meeting_id,
             'attendees': attendee})
