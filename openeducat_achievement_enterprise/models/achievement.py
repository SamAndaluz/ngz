# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields, api


class OpAchievement(models.Model):
    _name = "op.achievement"
    _inherit = ["mail.thread"]
    _rec_name = "student_id"
    _description = "Achievement"

    progression_id = fields.Many2one('op.student.progression',
                                     'Progression No')
    student_id = fields.Many2one('op.student', 'Student',
                                 required=True, track_visibility='onchange')
    faculty_id = fields.Many2one(
        'op.faculty', 'Faculty', required=True, track_visibility='onchange')
    achievement_type_id = fields.Many2one(
        'op.achievement.type', 'Achievement Type',
        required=True, track_visibility='onchange')
    description = fields.Text(
        'Description', required=True, track_visibility='onchange')
    achievement_date = fields.Date(
        'Date', required=True,
        default=fields.Date.today(), track_visibility='onchange')
    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id,
        track_visibility='onchange')
    active = fields.Boolean(default=True)

    @api.onchange('student_id')
    def onchange_student_achievement_progrssion(self):
        if self.student_id:
            student = self.env['op.student.progression'].search(
                [('student_id', '=', self.student_id.id)])
            self.progression_id = student.id
            sequence = student.name
            student.write({'name': sequence})


class OpStudent(models.Model):
    _inherit = "op.student"

    achievement_line_ids = fields.One2many(
        'op.achievement', 'student_id', 'Achievement Details')
