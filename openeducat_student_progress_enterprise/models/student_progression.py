# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields


class StudentProgression(models.Model):
    _name = "op.student.progression"
    _description = "Student progression"
    _inherit = ["mail.thread"]

    name = fields.Char('Sequence',
                       default=lambda self: self.env['ir.sequence'].
                       next_by_code('op.student.progression'),
                       copy=False, required=True)
    student_id = fields.Many2one('op.student',
                                 'Student', required=True,
                                 track_visibility="onchange")
    created_by = fields.Many2one('res.users', 'Created By',
                                 readonly=True,
                                 default=lambda self: self.env.uid,
                                 track_visibility="onchange")
    date = fields.Date('Date',
                       required=True,
                       default=fields.Date.today(),
                       track_visibility="onchange")

    state = fields.Selection([('draft', 'Draft'),
                              ('open', 'In Progress'),
                              ('done', 'Done'),
                              ('cancel', 'Cancel')],
                             string="Status", default='draft',
                             track_visibility="onchange")
    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id)
    active = fields.Boolean(default=True)

    def state_draft(self):
        self.state = "draft"

    def state_open(self):
        self.state = "open"

    def state_done(self):
        self.state = "done"

    def state_rejected(self):
        self.state = "cancel"

    _sql_constraints = [('student_id',
                         'unique(student_id)',
                         'Student already  exist!!!')]
