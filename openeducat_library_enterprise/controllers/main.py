# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

import calendar
from datetime import datetime, date

from odoo.exceptions import ValidationError
from odoo.http import request

from odoo import http
from odoo.addons.portal.controllers.portal import CustomerPortal


class LibraryPortal(CustomerPortal):

    @http.route(['/library/media/',
                 '/library/media/<int:student_id>'
                 '/library/media/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_student_library_media_list(self, student_id=None, **kw):

        media_id = request.env["op.media"].sudo().search([])

        return request.render(
            "openeducat_library_enterprise.openeducat_librart_midia_portal",
            {'library_ids': media_id})

    @http.route(['/library/media/<int:library_id>', ],
                type='http', auth="user", website=True)
    def portal_student_library_media_form(self, library_id):

        media_all_id = request.env['op.media'].sudo().search(
            [('id', '=', library_id)])

        return request.render(
            "openeducat_library_enterprise.openeducat_library_media_data",
            {'library_ids': media_all_id})

    @http.route(['/media/queue/request',
                 '/media/queue/request/<int:student_id>',
                 '/media/queue/request/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_library_queue_craete(self, student_id=None, **kw):

        user = request.env.user
        if student_id:
            student_queue_id = request.env['op.student'].sudo().search(
                [('user_id', '=', student_id)])
        else:
            student_queue_id = request.env['op.student'].sudo().search(
                [('user_id', '=', user.id)])

        media_data = request.env['op.media'].sudo().search([])

        return request.render(
            "openeducat_library_enterprise.openeducat_library_media_queue",
            {
                'student_ids': student_queue_id,
                'media_queue_ids': media_data,
                'date_from': datetime.today().strftime("%Y-%m-%d"),
            }
        )

    @http.route(['/queue/request/submit/',
                 '/queue/request/submit/<int:student_id>',
                 '/queue/request/submit/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_submit_media_queue_request(self, **kw):

        user = request.env.user
        vals = {
            'media_id': int(kw['media_ids']),
            'user_id': user.id,
            'date_to': kw['date_to'],
            'date_from': kw['date_from'],
        }
        try:
            media_id = request.env['op.media.queue'].sudo().create(vals)
            media_id.do_request_again()
        except ValidationError as e:
            raise e

        media_queue_dict = {}
        media_queue_dict.update()
        return request.render(
            "openeducat_library_enterprise.portal_submited_queue_request",
            {'media_ids': media_id})

    @http.route(['/requested/queue/list/',
                 '/requested/queue/list/<int:student_id>',
                 '/requested/queue/list/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_media_queue_requested_list(self, student_id=None, **kw):

        user = request.env.user
        if user.is_student:
            media_queue_id = request.env['op.media.queue'].sudo().search(
                [('user_id', '=', user.id)])
        else:
            student_id = request.env['op.student'].sudo().search(
                [('id', '=', student_id)])
            media_queue_id = request.env['op.media.queue'].sudo().search([
                ('user_id', '=', student_id.user_id.id)])

        return request.render(
            "openeducat_library_enterprise.portal_submited_queue_request_list",
            {'media_ids': media_queue_id})

    @http.route(['/media/purchase/request',
                 '/media/purchase/request/<int:student_id>/',
                 '/media/purchase/request/page/<int:student_id>/'],
                type='http', auth="user", website=True)
    def portal_library_media_purchase_create(self, student_id=None, **kw):

        user = request.env.user
        student_id = request.env['op.student'].sudo().search(
            [('user_id', '=', user.id)])
        media_course = request.env['op.course'].sudo().search([])
        media_subject = request.env['op.subject'].sudo().search([])
        media_type = request.env['op.media.type'].sudo().search([])

        media_purchase_dict = {}
        media_purchase_dict.update()

        return request.render(
            "openeducat_library_enterprise.openeducat_library_media_purchase",
            {
                'student_ids': student_id,
                'course_ids': media_course,
                'subject_ids': media_subject,
                'media_type_ids': media_type,
            }
        )

    @http.route(['/purchase/request/submit/',
                 '/purchase/request/submit/<int:student_id>',
                 '/purchase/request/submit/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_submit_media_purchase_request(self, **kw):

        partner = request.env.user.partner_id
        vals = {
            'name': kw['title'],
            'author': kw['authore'],
            'publisher': kw['publisher'],
            'edition': kw['edition'],
            'requested_id': partner.id,
            'course_ids': int(kw['media_ids']),
            'media_type_id': int(kw['media_type_ids']),
            'subject_ids': int(kw['subject_ids']),
        }
        media_id = request.env['op.media.purchase'].sudo().create(vals)
        media_id.act_requested()

        return request.render(
            "openeducat_library_enterprise.portal_submited_purchases_request",
            {'media_purchase_ids': media_id})

    @http.route(['/requested/purchase/list/',
                 '/requested/purchase/list/<int:student_id>',
                 '/requested/purchase/list/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_media_purchase_requested_list(self, student_id=None, **kw):

        user = request.env.user
        partner = request.env.user.partner_id
        if user.is_student:
            media_purchase_id = request.env['op.media.purchase'].sudo().search(
                [('requested_id', '=', partner.id)])
        else:
            student_id = request.env['op.student'].sudo().search(
                [('id', '=', student_id)])
            media_purchase_id = request.env[
                'op.media.purchase'].sudo().search(
                [('requested_id', '=', student_id.partner_id.id)])

        return request.render(
            "openeducat_library_enterprise."
            "portal_submited_purchase_request_list",
            {'purchase_ids': media_purchase_id})

    @http.route(['/media/movement/list/',
                 '/media/movement/list/<int:student_id>',
                 '/media/movement/list/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_media_movement_list(self, student_id=None, **kw):

        media_movement_id = request.env['op.media.movement'].sudo().search(
            [('student_id', '=', student_id)])

        return request.render(
            "openeducat_library_enterprise.portal_student_media_movement_list",
            {'media_movement_ids': media_movement_id})

    @http.route(['/media/movement/information/<int:media_movement_id>'],
                type='http', auth="user", website=True)
    def portal_media_movement_information(self, media_movement_id, **kw):

        media_movement = request.env['op.media.movement'].sudo().search(
            [('id', '=', media_movement_id)])

        return request.render(
            "openeducat_library_enterprise."
            "portal_student_media_movement_information",
            {'media_movement_ids': media_movement})


class OpenEduCatLibraryController(http.Controller):

    @http.route('/openeducat_library_enterprise/get_library_dashboard_data',
                type='json', auth='user')
    def compute_library_dashboard_data(self):
        dbt = 0
        dbm = 0
        tpat = 0

        media = request.env['ir.model'].search(
            [('model', '=', 'op.media')])
        if media:
            last_day = date.today().replace(
                day=calendar.monthrange(date.today().year,
                                        date.today().month)[1])
            dbt = request.env['op.media.movement'].search_count(
                [('state', '=', 'issue'), ('return_date', '=', date.today())])
            dbm = request.env['op.media.movement'].search_count([
                ('state', '=', 'issue'),
                ('return_date', '>=', date.today().strftime('%Y-%m-01')),
                ('return_date', '<=', last_day)])
            movements_ids = request.env['op.media.movement'].search(
                [('state', '=', 'return'),
                 ('return_date', '>=', date.today().strftime('%Y-%m-01')),
                 ('return_date', '<=', last_day)])
            for movement in movements_ids:
                tpat += movement.penalty
        return {'dbt': dbt, 'dbm': dbm, 'tpat': tpat}
