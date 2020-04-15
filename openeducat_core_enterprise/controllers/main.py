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

from odoo.http import request, Response

from odoo import fields
from odoo import http
from odoo.addons.portal.controllers.portal import CustomerPortal


class StudentPortal(CustomerPortal):

    def check_access_role(self, student):
        user = request.env.user.partner_id
        if student.partner_id.id != user.id:
            parent_list = []
            for parent in student.parent_ids:
                parent_list.append(parent.user_id.partner_id.id)
            if user.id in parent_list:
                return True
            else:
                return False
        else:
            return True

    def get_student(self, student_id=None, **kw):

        partner = request.env.user.partner_id
        student_obj = request.env['op.student']
        if not student_id:
            student = student_obj.sudo().search([
                ('partner_id', '=', partner.id)])
        else:
            student = student_obj.sudo().browse(student_id)

            access_role = self.check_access_role(student)
            if not access_role:
                return False

        return student

    @http.route(['/student/profile',
                 '/student/profile/<int:student_id>',
                 '/student/profile/page/<int:page>'],
                type='http', auth="user", website=True)
    def enterprise_portal_student_information(self, student_id=None):

        if student_id:
            student_data = self.get_student(student_id=student_id)
        else:
            student_data = self.get_student()

        if not student_data:
            return request.render('website.404')

        if student_data.partner_id.image_1920:
            student_img = student_data.partner_id.image_1920.decode("utf-8")
        else:
            student_img = student_data.partner_id.image_1920

        return request.render(
            "openeducat_core_enterprise.openeducat_enterprise_student_portal",
            {
                'student': student_data,
                'student_image': student_img
            })

    @http.route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        user = request.env.user
        values.update({
            'error': {},
            'error_message': [],
        })

        if post:
            error, error_message = self.details_form_validate(post)
            values.update({'error': error, 'error_message': error_message})
            values.update(post)
            if not error:
                values = {
                    key: post[key] for key in self.MANDATORY_BILLING_FIELDS}
                values.update(
                    {key: post[key]
                     for key in self.OPTIONAL_BILLING_FIELDS if key in post})
                values.update({'zip': values.pop('zipcode', '')})
                values.update({'country_id': int(values.pop('country_id'))})
                values.update({'state_id': (values.pop('state_id')) or False})
                partner.sudo().write(values)
                if user.is_parent:
                    return request.redirect('/my/child')
                else:
                    return request.redirect('/my/home')
        countries = request.env['res.country'].sudo().search([])
        states = request.env['res.country.state'].sudo().search([])
        values.update({
            'partner': partner,
            'countries': countries,
            'states': states,
            'has_check_vat': hasattr(request.env['res.partner'], 'check_vat'),
            'redirect': redirect,
            'page_name': 'my_details',
        })

        response = request.render("portal.portal_my_details", values)
        response.headers['X-Frame-Options'] = 'DENY'
        return response


class OpenEduCatController(http.Controller):

    @http.route('/openeducat_core_enterprise/get_main_dash_data',
                type='json', auth='user')
    def compute_main_dashboard_data(self):
        ser = 0
        es = 0
        mfr = '0:0'
        spr = 0

        adm_ref = request.env['op.admission']
        student_ref = request.env['op.student']
        admission = request.env['ir.model'].search(
            [('model', '=', 'op.admission')])
        if admission:
            total_admsn = adm_ref.search_count([
                ('state', '=', 'done')])
            if total_admsn:
                ser = round(total_admsn * 100 / adm_ref.search_count([]), 2)
                es = adm_ref.search_count([('state', '=', 'done')])
        m_student = student_ref.search_count([('gender', '=', 'm')])
        f_student = student_ref.search_count([('gender', '=', 'f')])
        mfr = str(m_student) + ':' + str(f_student)
        total_faculty = request.env['op.faculty'].search_count([])
        spr = str(m_student + f_student) + ':' + str(total_faculty)
        return {'student_enroll_rate': ser, 'erolled_students': es,
                'mf_ratio': mfr, 'sp_ratio': spr}

    @http.route('/openeducat_core_enterprise/fetch_batch',
                type='json', auth='user')
    def fetch_openeducat_batches(self):
        return {'batch_ids': request.env['op.batch'].search_read(
            [], ['id', 'name'], order='name')}

    @http.route('/openeducat_core_enterprise/compute_openeducat_batch_graph',
                type='json', auth='user')
    def compute_openeducat_batch_graph(self, batch_id):
        data = []
        last_day = datetime.today().replace(
            day=calendar.monthrange(date.today().year,
                                    date.today().month)[1])
        for d in range(1, last_day.day + 1):
            attendance_sheet = request.env['ir.model'].search(
                [('model', '=', 'op.attendance.sheet')])
            if attendance_sheet and batch_id:
                value = request.env['op.attendance.sheet'].search([
                    ('batch_id', '=', int(batch_id)),
                    ('attendance_date', '=',
                     fields.date.today().replace(day=d))])
                data.append({'label': str(d),
                             'value': value and value[0].total_present or 0})
        return data

    @http.route('/openeducat_core_enterprise/get_batch_dashboard_data',
                type='json', auth='user')
    def compute_batch_dashboard_data(self, batch_id):
        tar = 0
        ts = 0
        tbl = 0
        ta = 0
        ir_model_ref = request.env['ir.model']
        op_attn_sheet_ref = request.env['op.attendance.sheet']
        attendance_sheet = ir_model_ref.search([
            ('model', '=', 'op.attendance.sheet')])
        if attendance_sheet and batch_id:
            tarp = op_attn_sheet_ref.search(
                [('batch_id', '=', int(batch_id)),
                 ('attendance_date', '=', fields.date.today())])
            tara = op_attn_sheet_ref.search(
                [('batch_id', '=', int(batch_id)),
                 ('attendance_date', '=', fields.date.today())])
            tar = tarp and str(tarp[0].total_present) or '0'
            tar += ':'
            tar += tara and str(tara[0].total_absent) or '0'
        if batch_id:
            ts = request.env['op.student'].search_count([
                ('course_detail_ids.batch_id', '=', int(batch_id))])
        session = ir_model_ref.search([('model', '=', 'op.session')])
        if session and batch_id:
            tbl = request.env['op.session'].search_count(
                [('batch_id', '=', int(batch_id)),
                 ('start_datetime', '>=',
                  datetime.today().strftime('%Y-%m-%d 00:00:00')),
                 ('start_datetime', '<=',
                  datetime.today().strftime('%Y-%m-%d 23:59:59'))])
        assignment = ir_model_ref.search([('model', '=', 'op.assignment')])
        if assignment and batch_id:
            ta = request.env['op.assignment'].search_count(
                [('batch_id', '=', int(batch_id))])
        return {'tar': tar, 'tbl': tbl, 'ts': ts, 'ta': ta}

    @http.route(['/subject/registration/',
                 '/subject/registration/<int:student_id>',
                 '/subject/registration/page/<int:page>'],
                type='http', auth='user', website=True)
    def portal_student_subject_registration_list(self, student_id=None):

        user = request.env.user
        if student_id:
            subject_registration_id = request.env[
                'op.subject.registration'].sudo().search(
                [('student_id', '=', student_id)])
        else:
            student_id = request.env['op.student'].sudo().search(
                [('user_id', '=', user.id)])
            subject_registration_id = request.env[
                'op.subject.registration'].sudo().search(
                [('student_id', '=', student_id.id)])

        return request.render(
            "openeducat_core_enterprise."
            "portal_student_subject_registration_list",
            {
                'subject_registration_ids': subject_registration_id,
            }
        )

    def check_subject_registration_access(self, reg_id=None):

        registration_id = request.env['op.subject.registration'].sudo().search(
            [('id', '=', reg_id)])

        user = request.env.user
        user_list = []
        count = 0
        for rec in registration_id.student_id:
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

    @http.route(['/subject/registration/data/<int:reistration_id>'],
                type='http', auth='user', website=True)
    def portal_student_subject_registration_data(self, reistration_id=None):

        subject_registration_id = request.env[
            'op.subject.registration'].sudo().search(
            [('id', '=', reistration_id)])

        access_role = self.check_subject_registration_access(subject_registration_id.id)
        if access_role is False:
            return Response("[Bad Request]", status=404)

        return request.render(
            "openeducat_core_enterprise."
            "portal_student_subject_registration_data",
            {'subject_register_ids': subject_registration_id})

    @http.route(['/subject/registration/create/',
                 '/subject/registration/create/<int:student_id>',
                 '/subject/registration/create/<int:page>'],
                type='http', auth="user", website=True)
    def portal_craete_subject_registration(self, student_id=None, **kw):

        user = request.env.user
        student_id = request.env['op.student'].sudo().search([
            ('user_id', '=', user.id)])

        elective_subjects = request.env['op.subject'].sudo().search(
            [('subject_type', '=', 'elective')])

        course_ids = request.env['op.course'].sudo().search([])
        batch_ids = request.env['op.batch'].sudo().search([])

        return request.render(
            "openeducat_core_enterprise."
            "openeducat_create_subject_registration",
            {'student_id': student_id,
             'subject_registration_ids': elective_subjects,
             'course_ids': course_ids,
             'batch_ids': batch_ids,
             })

    @http.route(['/subject/registration/submit',
                 '/subject/registration/submit/<int:page>'],
                type='http', auth="user", website=True)
    def portal_submit_subject_registration(self, **kw):

        compulsory_subject = request.httprequest. \
            form.getlist('compulsory_subject_ids')
        elective_subject = request.httprequest. \
            form.getlist('elective_subject_ids')

        vals = {
            'student_id': kw['student_id'],
            'course_id': kw['course_id'],
            'batch_id': kw['batch_id'],
            'min_unit_load': kw['min_unit_load'],
            'max_unit_load': kw['max_unit_load'],
            'compulsory_subject_ids': [[6, 0, compulsory_subject]],
            'elective_subject_ids': [[6, 0, elective_subject]],
        }
        registration_id = request.env['op.subject.registration']
        registration_id.sudo().create(vals).action_submitted()

        return request.redirect('/subject/registration/')

    @http.route(['/get/course_data'],
                type='json', auth="none", website=True)
    def get_course_data(self, course_id, **kw):
        batch_list = []
        subject_list = []
        batch_ids = request.env['op.batch'].sudo().search(
            [('course_id', '=', int(course_id))])
        subject_ids = request.env['op.subject'].sudo().search([
            ('course_id', '=', int(course_id))])
        if batch_ids:
            for batch_id in batch_ids:
                batch_list.append({'name': batch_id.name,
                                   'id': batch_id.id})
        if subject_ids:
            for subject_id in subject_ids:
                subject_list.append({'name': subject_id.name,
                                     'id': subject_id.id})
        return {'batch_list': batch_list,
                'subject_list': subject_list}
