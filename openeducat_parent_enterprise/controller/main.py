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


class ParentCorePotal(CustomerPortal):

    @http.route(['/my/child/<int:child_id>'],
                type='http', auth="user", website=True)
    def portal_child_detail(self, child_id=None, **kw):
        values = self._prepare_portal_layout_values()
        student_id = request.env['op.student'].sudo().search(
            [('id', '=', child_id)])

        access_role = self.check_access_role(student_id)
        if not access_role:
            return request.render("website.404")

        values.update({'is_parent': True,
                       'student_id': str(student_id.id),
                       'stu_id': student_id})

        return request.render("portal.portal_my_home", values)

    @http.route(['/my/child',
                 '/my/child/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_child_parent(self, **kw):
        user = request.env.user
        parent = request.env['op.parent'].sudo().search([
            ('user_id', '=', user.id)])

        return request.render(
            "openeducat_parent_enterprise.portal_children_data",
            {'child_ids': parent.student_ids})
