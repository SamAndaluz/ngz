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


class MeetingPortal(CustomerPortal):

    @http.route(['/meeting/information/',
                 '/meeting/information/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_meeting_list(self, **kw):

        meeting_id = request.env["op.meeting"].sudo().search([])

        return request.render(
            "openeducat_meeting_enterprise.openeducat_meeting_portal",
            {'meeting_ids': meeting_id})

    @http.route(['/meeting/information/<int:meeting_id>', ],
                type='http', auth="user", website=True)
    def portal_meeting_form(self, meeting_id, **kw):

        meeting_all_id = request.env['op.meeting'].sudo().search(
            [('id', '=', meeting_id)])

        return request.render(
            "openeducat_meeting_enterprise.openeducat_meeting_portal_data",
            {'meeting_ids': meeting_all_id})
