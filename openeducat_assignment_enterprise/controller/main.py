# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from datetime import datetime
import base64
import io
from odoo.http import request, Response
from odoo.tools import consteq, plaintext2html
from werkzeug.exceptions import NotFound, Forbidden
from odoo import http
from odoo.addons.portal.controllers.portal import CustomerPortal


def _has_token_access(res_model, res_id, token=''):
    record = request.env[res_model].browse(res_id).sudo()
    token_field = request.env[res_model]._mail_post_token_field
    return (token and record and consteq(record[token_field], token))


def _message_post_helper(res_model='', res_id=None, message='',
                         token='', nosubscribe=True, **kw):
    """ Generic chatter function, allowing to write on *any*
     object that inherits mail.thread.
        If a token is specified, all logged in users will be
         able to write a message regardless
        of access rights; if the user is the public user,
         the message will be posted under the name
        of the partner_id of the object (or the public user
         if there is no partner_id on the object).

        :param string res_model: model name of the object
        :param int res_id: id of the object
        :param string message: content of the message

        optional keywords arguments:
        :param string token: access token if the object's
         model uses some kind of public access
                             using tokens (usually a uuid4)
                              to bypass access rules
        :param bool nosubscribe: set False if you want the
         partner to be set as follower of the object when posting
          (default to True)

        The rest of the kwargs are passed on to message_post()
    """
    record = request.env[res_model].browse(res_id)
    author_id = request.env.user.partner_id.id if \
        request.env.user.partner_id else False

    if token:
        access_as_sudo = _has_token_access(res_model, res_id, token=token)
        if access_as_sudo:
            record = record.sudo()
            if request.env.user._is_public():
                if kw.get('pid') and \
                        consteq(kw.get('hash'),
                                record._sign_token(int(kw.get('pid')))):
                    author_id = kw.get('pid')
                else:
                    # TODO : After adding the pid and sign_token in access_url
                    #  when send invoice by email, remove this line
                    # TODO : Author must be Public User
                    #  (to rename to 'Anonymous')
                    author_id = record.partner_id.id if hasattr(
                        record, 'partner_id'
                    ) and record.partner_id.id else author_id
            else:
                if not author_id:
                    raise NotFound()
    else:
        if not (request.env.user.is_student or request.env.user.is_parent):
            raise Forbidden()
    kw.pop('csrf_token', None)
    kw.pop('attachment_ids', None)
    return record.with_context(
        mail_create_nosubscribe=nosubscribe).sudo().message_post(
        body=message,
        message_type=kw.pop('message_type', "comment"),
        subtype=kw.pop('subtype', "mt_comment"),
        author_id=author_id, **kw)


class SubmitAssignment(CustomerPortal):

    @http.route(['/mail/chatter_post'],
                type='http', methods=['POST'], auth='public', website=True)
    def portal_chatter_post(self, res_model, res_id, message, **kw):

        url = request.httprequest.referrer
        if message:
            # message is received in plaintext and saved in html
            message = plaintext2html(message)
            _message_post_helper(res_model, int(res_id), message, **kw)
            url = url + "#discussion"

        return request.redirect(url)

    @http.route(['/assignment/submit',
                 '/assignment/submit/<int:student_id>',
                 '/assignment/submit/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_submit_assignment(self, student_id=None, **kw):
        user = request.env.user
        assignment_list = []

        if not student_id:
            student = request.env['op.student'].sudo().search([
                ('user_id', '=', user.id)])
            for assignment in student.allocation_ids:
                if assignment.state not in ['finish', 'draft']:
                    assignment_list.append(assignment)
        else:
            student = request.env['op.student'].sudo().search([
                ('id', '=', student_id)])
            for assignment in student.allocation_ids:
                if assignment.state not in ['finish']:
                    assignment_list.append(assignment)

            access_role = self.check_access_role(assignment_list)
            if not access_role:
                return False

        return request.render(
            "openeducat_assignment_enterprise."
            "portal_student_submit_assignment_data",
            {
                'student_ids': student,
                'assignment_ids': assignment_list,
                'submit_date': datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
            })

    @http.route(['/assignment/submited',
                 '/assignment/submited/<int:student_id>',
                 '/assignment/submited/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_submit_assignment_create(self, **kw):
        vals = {
            'student_id': int(kw['stud_id']),
            'submission_date': kw['Date'],
            'assignment_id': int(kw.get('assignment_id')),
            'description': kw['Description'],
            'note': kw['Note'],
        }
        assignment_id = request.env[
            'op.assignment.sub.line'].sudo().create(vals)
        assignment_id.act_submit()

        if 'attachments' in request.params:
            attached_files = request.httprequest.files.getlist('attachments')
            for attachment in attached_files:
                attached_file = attachment.read()
                request.env['ir.attachment'].sudo().create({
                    'name': attachment.filename,
                    'res_model': 'op.assignment.sub.line',
                    'res_id': assignment_id,
                    'type': 'binary',
                    # 'name': attachment.filename,
                    'datas': base64.encodestring(attached_file),
                })

        return request.render(
            "openeducat_assignment_enterprise."
            "portal_submited_assignment_of_student",
            {'assignment_ids': assignment_id})

    @http.route(['/submited/assignment/list',
                 '/submited/assignment/list/<int:student_id>',
                 '/submited/assignment/list/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_submit_assignment_list(self, student_id=None):
        user = request.env.user

        if user.is_student:
            assignment_id = request.env[
                'op.assignment.sub.line'].sudo().search(
                [('user_id', '=', user.id)])
        else:
            assignment_id = request.env[
                'op.assignment.sub.line'].sudo().search(
                [('student_id', '=', student_id)])

        return request.render(
            "openeducat_assignment_enterprise.portal_submited_assignment_list",
            {'assignment_ids': assignment_id})

    def check_submission_access(self, submission_id=None):
        submission = request.env['op.assignment.sub.line'].sudo().search(
            [('id', '=', submission_id)])

        user = request.env.user
        user_list = []
        count = 0
        for rec in submission.student_id:
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

    @http.route(['/assignment/data/<int:assignment_id>',
                 '/assignment/data/<int:assignment_id>/page/<int:page>'],
                type='http', auth="user", website=True)
    def portal_submited_assignment_data(self, assignment_id=None):

        submission_instance = request.env[
            'op.assignment.sub.line'].sudo().search(
            [('id', '=', assignment_id)])
        attachment_instance = submission_instance.attachment_ids
        access_role = self.check_submission_access(submission_instance.id)
        if access_role is False:
            return Response("[Bad Request]", status=404)

        return request.render(
            "openeducat_assignment_enterprise.assignment_data", {
                'assignment_ids': submission_instance,
                'attachment_ids': attachment_instance,
            })

    @http.route(['/assignment/submission/download/<int:attachment_id>'],
                type='http', auth='user', website=True)
    def download_submission_attachment(self, attachment_id):

        attachment = request.env['ir.attachment'].sudo().search_read(
            [('id', '=', int(attachment_id))],
            ["name", "datas", "res_model", "res_id", "type", "url"]
        )
        if attachment:
            attachment = attachment[0]
        res_id = attachment['res_id']
        submission_id = request.env['op.assignment.sub.line'].sudo().search(
            [('id', '=', res_id)])
        access_role = self.check_submission_access(submission_id.id)
        if access_role is False:
            return Response("[Bad Request]", status=404)

        if submission_id:
            if attachment["type"] == "url":
                if attachment["url"]:
                    return http.redirect_with_hash(attachment["url"])
                else:
                    return request.not_found()
            elif attachment["datas"]:
                data = io.BytesIO(base64.standard_b64decode(
                    attachment["datas"]))
                return http.send_file(
                    data, filename=attachment['name'], as_attachment=True)
            else:
                return request.not_found()

    def check_assignment_access(self, assignment_id=None):

        assignment = request.env['op.assignment'].sudo().search(
            [('id', '=', assignment_id)])

        user = request.env.user
        user_list = []
        count = 0
        for rec in assignment.allocation_ids:
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

    @http.route(['/assignment/details/<int:assignment_id>'],
                type='http', auth='user', website=True)
    def assignment_details(self, assignment_id=None):

        assignment = request.env['op.assignment'].sudo().search(
            [('id', '=', assignment_id)])

        access_role = self.check_assignment_access(assignment.id)
        if access_role is False:
            return Response("[Bad Request]", status=404)

        return request.render(
            "openeducat_assignment_enterprise.assignment_details",
            {'assignment': assignment})

    @http.route(['/assignment/attachment/download/<int:attachment_id>'],
                type='http', auth='user', website=True)
    def download_assignment_attachment(self, attachment_id):
        attachment = request.env['ir.attachment'].sudo().search_read(
            [('id', '=', int(attachment_id))],
            ["name", "datas", "res_model", "res_id", "type", "url"])
        if attachment:
            attachment = attachment[0]
        res_id = attachment['res_id']
        assignment_id = request.env['op.assignment'].sudo().search(
            [('id', '=', res_id)])

        access_role = self.check_assignment_access(assignment_id.id)
        if access_role is False:
            return Response("[Bad Request]", status=404)

        if assignment_id:
            if attachment["type"] == "url":
                if attachment["url"]:
                    return http.redirect_with_hash(attachment["url"])
                else:
                    return request.not_found()
            elif attachment["datas"]:
                data = io.BytesIO(base64.standard_b64decode(
                    attachment["datas"]))
                return http.send_file(
                    data, filename=attachment['name'], as_attachment=True)
            else:
                return request.not_found()

    @http.route(['/student/assignment/details',
                 '/student/assignment/details/<int:student_id>'],
                type='http', auth='user', website=True)
    def student_assignment_details(self, student_id=None):
        if student_id:
            student_data = self.get_student(student_id=student_id)
        else:
            student_data = self.get_student()

        if not student_data:
            return request.render('website.404')

        return request.render(
            "openeducat_assignment_enterprise.openeducat_student_assignments",
            {
                'student': student_data,
            })
