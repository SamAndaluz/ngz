# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields, api


class OpAssignmentSubLine(models.Model):
    _inherit = "op.assignment.sub.line"

    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id)

    progression_id = fields.Many2one('op.student.progression',
                                     string="Progression No")
    attachment_ids = fields.One2many('ir.attachment', 'res_id',
                                     domain=[('res_model', '=',
                                              'op.assignment.sub.line')],
                                     string='Attachments',
                                     readonly=True)

    def student_submission(self):
        result = self.sudo().act_submit()
        return result and result or False

    @api.onchange('student_id')
    def onchange_student_assignment_progrssion(self):
        if self.student_id:
            student = self.env['op.student.progression'].search(
                [('student_id', '=', self.student_id.id)])
            self.progression_id = student.id
            sequence = student.name
            student.write({'name': sequence})

    def search_read_for_app(self, offset=0, limit=None, order=None):

        if self.env.user.partner_id.is_student:
            domain = [('user_id', '=', self.env.user.id)]
            fields = ['student_id', 'assignment_id', 'submission_date',
                      'state', 'description', 'note', 'marks']
            res = self.sudo().search_read(domain=domain, fields=fields,
                                          offset=offset, limit=limit, order=order)
            return res

        elif self.user_has_groups('openeducat_core.group_op_faculty'):
            fields = ['student_id', 'assignment_id', 'submission_date',
                      'state', 'description', 'note', 'marks']
            res = self.sudo().search_read(domain=[], fields=fields,
                                          offset=offset, limit=limit, order=order)
            return res
