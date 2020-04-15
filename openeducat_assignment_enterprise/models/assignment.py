# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields, _
from odoo.exceptions import ValidationError


class OpAssignment(models.Model):
    _inherit = "op.assignment"

    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id)

    attachment_ids = fields.One2many('ir.attachment', 'res_id',
                                     domain=[('res_model', '=',
                                              'op.assignment')],
                                     string='Attachments',
                                     readonly=True)

    def unlink(self):
        for record in self:
            if not record.state == 'draft' and not self.env.user.has_group(
                    'openeducat_core.group_op_faculty'):
                raise ValidationError(
                    _("You can't delete none draft submissions!"))
        res = super(OpAssignment, self).unlink()
        return res

    def write(self, vals):
        if self.env.user.child_ids:
            raise Warning(_('Invalid Action!\n Parent can not edit \
               Assignment Submissions!'))
        return super(OpAssignment, self).write(vals)

    def search_read_for_app(self, offset=0, limit=None, order=None):
        if self.env.user.partner_id.is_student:
            partner = self.env.user.partner_id
            domain = ([('state', '=', 'publish'),
                       ('allocation_ids.partner_id', '=', partner.id)])
            fields = ['name', 'batch_id', 'course_id', 'subject_id',
                      'assignment_type_id', 'faculty_id', 'issued_date',
                      'submission_date', 'marks', 'allocation_ids',
                      'state', 'description']
            res = self.sudo().search_read(domain=domain, fields=fields,
                                          offset=offset, limit=limit, order=order)
            return res

        elif self.env.user.partner_id.is_parent:
            user = self.env.user
            parent_id = self.env['op.parent'].sudo().search(
                [('user_id', '=', user.id)])

            student_id = [student.id for student in parent_id.student_ids]
            domain = [('allocation_ids', 'in', student_id)]
            fields = ['name', 'batch_id', 'course_id', 'subject_id',
                      'assignment_type_id', 'faculty_id', 'issued_date',
                      'submission_date', 'marks', 'allocation_ids', 'description']
            res = self.sudo().search_read(domain=domain, fields=fields,
                                          offset=offset, limit=limit, order=order)
            return res

        elif self.user_has_groups('openeducat_core.group_op_faculty'):
            user = self.env.user
            faculty_id = self.env['op.faculty'].sudo().search(
                [('user_id', '=', user.id)])
            domain = [('faculty_id', '=', faculty_id.id)]
            fields = ['name', 'batch_id', 'course_id', 'subject_id',
                      'assignment_type_id', 'faculty_id', 'issued_date',
                      'submission_date', 'marks', 'allocation_ids',
                      'description', 'state']
            res = self.sudo().search_read(domain=domain, fields=fields,
                                          offset=offset, limit=limit, order=order)
            return res
