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
from odoo.addons.portal.controllers.portal import \
    CustomerPortal


class AlumaniJobPost(CustomerPortal):

    @http.route(['/alumni/job',
                 '/alumni/job/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_alumni_job_post(self, **kw):
        emp_type = request.env['op.job.type'].sudo().search([])
        skill_obj = request.env['op.skill'].sudo().search([])
        skill_ids = [skill_id for skill_id in skill_obj]
        country_id = request.env['res.country'].sudo().search([])
        state_id = request.env['res.country.state'].sudo().search([])

        return request.render(
            "openeducat_alumni_job_enterprise.portal_student_alumni_job",
            {'emp_type': emp_type,
             'skill_obj': skill_ids,
             'country_obj': country_id,
             'state_obj': state_id})

    @http.route(['/alumni/job/submit',
                 '/alumni/job/submit/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_alumni_job_post_submit(self, **kw):
        vals = {
            'job_post': kw['job_post'],
            'salary_from': kw['salary_from'],
            'salary_upto': kw['salary_upto'],
            'street': kw['street'],
            'street2': kw['street'],
            'city': kw['city'],
            'start_date': kw['start_date'],
            'end_date': kw['end_date'],
            'created_by': kw['created_by'],
            'payable_at': kw['payable_at'],
            'expected_employees': kw['expected_employees'],
            'description': kw['description'],
            'employment_type': kw['employment_type'],
            'zip': kw['zip'],
            'country_id': kw['country_id'],
            # 'state_id': kw['state_id'],
            'skill_ids': [
                [6, 0, request.httprequest.form.getlist('skill_ids')]
            ]
        }
        request.env['op.job.post'].sudo().create(vals)
        return request.redirect("/alumni/job/list")

    @http.route(['/alumni/job/list',
                 '/alumni/job/list/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_alumni_job_post_list(self, **kw):
        alumni_obj = request.env['op.job.post'].sudo().search([])

        return request.render(
            "openeducat_alumni_job_enterprise.portal_student_alumni_job_list",
            {'alumni': alumni_obj})

    @http.route(['/alumni/job/details/<int:alumni_id>',
                 '/alumni/job/details/<int:alumni_id>/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_alumni_job_post_list_details(self, alumni_id, **kw):
        alumni_obj = request.env['op.job.post'].sudo().search(
            [('id', '=', alumni_id)])

        return request.render(
            "openeducat_alumni_job_enterprise.porta_alumni_list_details",
            {'alumni_data': alumni_obj})

    @http.route(['/alumni/job/delete/<int:alumni>',
                 '/alumni/job/delete/page/<int:page>'],
                type='http', auth="user", website=True)
    def delete_alumni(self, alumni):
        delete_id = request.env['op.job.post']\
            .sudo().search([('id', '=', alumni)])
        delete_id.unlink()
        return request.redirect('/alumni/job/list')

    @http.route(['/alumni/job/data/<int:alumni_id>',
                 '/alumni/job/data/<int:alumni_id>/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_alumni_job_post_list_data(self, alumni_id, **kw):
        alumni_obj = request.env['op.job.post'].sudo().search(
            [('id', '=', alumni_id)])

        emp_type = request.env['op.job.type'].sudo().search([])
        skill_obj = request.env['op.skill'].sudo().search([])
        skill_ids = [skill_id for skill_id in skill_obj]
        country_id = request.env['res.country'].sudo().search([])
        state_id = request.env['res.country.state'].sudo().search([])

        return request.render(
            "openeducat_alumni_job_enterprise.portal_alumni_job_list_data",
            {'alumni_data': alumni_obj,
             'emp_type': emp_type,
             'skill_obj': skill_ids,
             'country_obj': country_id,
             'state_obj': state_id})

    @http.route(['/alumni/job/update/<int:alumni_id>',
                 '/alumni/job/update/<int:alumni_id>/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_alumni_job_post_data_edit(self, alumni_id, **kw):
        skills_data = request.httprequest.form.getlist('skill_ids')
        vals = {
            'job_post': kw['job_post'],
            'salary_from': kw['salary_from'],
            'salary_upto': kw['salary_upto'],
            'street': kw['street'],
            'street2': kw['street'],
            'city': kw['city'],
            'start_date': kw['start_date'],
            'end_date': kw['end_date'],
            'created_by': kw['created_by'],
            'payable_at': kw['payable_at'],
            'expected_employees': kw['expected_employees'],
            'description': kw['description'],
            'employment_type': kw['employment_type'],
            'zip': kw['zip'],
            'country_id': kw['country_id'],
            'state_id': kw['state_id'],
            'skill_ids': [(6, 0, [int(g) for g in skills_data])]
        }

        alumni_post_id = request.env['op.job.post'].sudo().search(
            [('id', '=', alumni_id)]
        )
        alumni_post_id.sudo().write(vals)
        return request.redirect("/alumni/job/list")

    @http.route(['/get/country_data'],
                type='json', auth="none", website=True)
    def get_country_data(self, country_id, **kw):
        state_list = []
        state_ids = request.env['res.country.state'].sudo().search(
            [('country_id', '=', int(country_id))])

        for i in state_ids:
            state_list.append({'id': i.id, 'name': i.name})

        return {'state_list': state_list}
