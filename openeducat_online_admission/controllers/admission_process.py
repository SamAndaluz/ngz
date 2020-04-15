# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT

from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.http import request


class AdmissionRegistration(http.Controller):

    @http.route(['/admissionregistration'], type='http',
                auth='public', website=True)
    def admission_registration(self, **post):
        register_ids = request.env['op.admission.register'].sudo().search(
            [('state', '=', 'application')])
        country_ids = request.env['res.country'].sudo().search([])
        student_id = request.env['op.student'].sudo().search([
            ('partner_id', '=', request.env.user.partner_id.id)])
        post.update({
            'register_ids': register_ids,
            'countries': country_ids,
            'student_id': student_id,
            'partner_id': request.env.user.partner_id,
        })
        return request.render(
            "openeducat_online_admission.admission_registration", post)

    @http.route(['/get/application_data'],
                type='json', auth="none", website=True)
    def get_application_data(self, application, **kw):

        student_id = request.env['op.student'].sudo().search_read(
            domain=[('partner_id', '=', int(application))],
            fields=['first_name', 'middle_name', 'last_name',
                    'gender', 'email', 'mobile', 'phone', 'street', 'city',
                    'zip', 'country_id', 'birth_date', 'partner_id', 'user_id'])

        country_id = request.env['res.country'].sudo().search_read(domain=[],
                                                                   fields=['name'])

        if application != '0':
            return {'student_id': student_id,
                    'country_id': country_id}
        else:
            return {'country': country_id}


class WebsiteSale(WebsiteSale):

    @http.route()
    def confirm_order(self, **post):
        val = post.copy()
        admission_id = False
        if val and val.get('register_id', False):
            register = request.env['op.admission.register'].sudo().search(
                [('id', '=', int(val['register_id']))])
            product_id = register.product_id
            lst_price = register.product_id.lst_price
            val.update({'register_id': register.id,
                        'course_id': register.course_id.id,
                        'application_date': datetime.today(),
                        'fees': product_id and lst_price or 0.0,
                        'name': post.get('first_name') + ' ' + post.get(
                            'middle_name') + ' ' + post.get('last_name'),
                        'fees_term_id': register.course_id.fees_term_id.id,
                        'student_id': post.get('student_id'),
                        'state': 'online'})

            if not val['student_id']:
                lang = request.env['ir.qweb.field'].user_lang()
                val['birth_date'] = datetime.strptime(
                    val['birth_date'],
                    lang.date_format).strftime(DEFAULT_SERVER_DATE_FORMAT)
            admission_id = request.env['op.admission'].sudo().create(val)
            prod_id = False
            if register.course_id.reg_fees:
                prod_id = register.course_id.product_id.id
            else:
                return request.render(
                    "openeducat_online_admission.application_confirmed",
                    {'admission_id': admission_id})
            add_qty = 1
            set_qty = 0
            request.website.sale_get_order(force_create=1)._cart_update(
                product_id=int(prod_id), add_qty=float(add_qty),
                set_qty=float(set_qty))

            order = request.website.sale_get_order()

            redirection = self.checkout_redirection(order)
            if redirection:
                return redirection

            if order.partner_id.id == \
                    request.website.user_id.sudo().partner_id.id:
                return request.redirect('/shop/address')

            for f in self._get_mandatory_billing_fields():
                if not order.partner_id[f]:
                    return request.redirect(
                        '/shop/address?partner_id=%d' % order.partner_id.id)

            values = self.checkout_values(**post)

            if post.get('express'):
                return request.redirect('/shop/confirm_order')

            values.update({'website_sale_order': order})

            # Avoid useless rendering if called in ajax
            if post.get('xhr'):
                return 'ok'
            return request.render("website_sale.checkout", values)

        order = request.website.sale_get_order()
        if not order:
            return request.redirect("/shop")
        if order and admission_id:
            admission_id.write({'order_id': order.id})
            if request.env.uid:
                user = request.env['res.users'].browse(request.env.uid)
                partner_id = user.partner_id.id
            else:
                partner_id = request.env['res.partner'].sudo().create(post).id
            order.write({'partner_invoice_id': partner_id,
                         'partner_id': partner_id})
        redirection = self.checkout_redirection(order)
        if redirection:
            return redirection
        order.onchange_partner_shipping_id()
        order.order_line._compute_tax_id()
        request.session['sale_last_order_id'] = order.id
        request.website.sale_get_order(update_pricelist=True)
        extra_step = request.env.ref('website_sale.extra_info_option')
        if extra_step.active:
            return request.redirect("/shop/extra_info")
        return request.redirect("/shop/payment")


class StudentRegistration(http.Controller):

    @http.route(['/student/registration/info/'], type='http',
                auth='public', website=True)
    def studnet_registration_list_data123(self):
        user = request.env.user.partner_id
        student = request.env['op.student'].sudo().search([
            ('partner_id', '=', user.id)])
        register_ids = request.env['op.admission'].sudo().search(
            ['|', ('create_uid', '=', user._uid), ('student_id', '=', student.id)])

        return request.render(
            "openeducat_online_admission.openeducat_student_registration_list_data",
            {'registration_id': register_ids})
