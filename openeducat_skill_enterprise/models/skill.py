# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields


class Opskill(models.Model):
    _name = "op.skill"
    _description = "Skills Creation"

    name = fields.Char('Name', size=64, required=True)
    code = fields.Char('Code', size=64, required=True)
    skill_category_type_id = fields.Many2one(
        'op.skill.category', string='Skill Type', required=True)


class Opskillline(models.Model):
    _name = "op.skill.line"
    _description = "Skill Lines Creation Creation"

    skill_type_id = fields.Many2one('op.skill', string='Skill', required=True)
    student_id = fields.Many2one('op.student', string='student')
    rating = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')], 'Rating', default='1', required=True)


class OpStudent(models.Model):
    _inherit = "op.student"

    skill_line = fields.One2many(
        'op.skill.line', 'student_id', 'Skills Details')
