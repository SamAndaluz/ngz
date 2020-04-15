# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields


class OpPlacementOffer(models.Model):
    _name = "op.placement.offer"
    _inherit = "mail.thread"
    _description = "Placement Offer"

    name = fields.Char('Company Name', required=True)
    student_id = fields.Many2one('op.student', 'Student Name', required=True)
    join_date = fields.Date('Join Date', default=fields.Date.today())
    offer_package = fields.Char('Offered Package', size=256)
    training_period = fields.Char('Training Period', size=256)
    state = fields.Selection(
        [('draft', 'Draft'), ('offer', 'Offer'), ('join', 'Join'),
         ('reject', 'Rejected'), ('cancel', 'Cancel')], 'State',
        default='draft', track_visibility='onchange')
    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id)

    def placement_offer(self):
        self.state = 'offer'

    def placement_join(self):
        self.state = 'join'

    def confirm_rejected(self):
        self.state = 'reject'

    def confirm_to_draft(self):
        self.state = 'draft'

    def confirm_cancel(self):
        self.state = 'cancel'


class OpStudent(models.Model):
    _inherit = "op.student"

    placement_line = fields.One2many(
        'op.placement.offer', 'student_id', 'Placement Details')

    placement_count = fields.Integer(compute='_compute_placement_count')

    def get_placement(self):
        action = self.env.ref('openeducat_placement_enterprise.'
                              'act_open_op_placement_offer_view').read()[0]
        action['domain'] = [('student_id', 'in', self.ids)]
        return action

    def _compute_placement_count(self):
        for record in self:
            record.placement_count = self.env['op.placement.offer'].search_count(
                [('student_id', 'in', self.ids)])
