# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields, api


class StudentProgression(models.Model):
    _inherit = ["op.student.progression"]

    @api.depends("activity_lines")
    def _compute_total_activity(self):
        self.total_activity = len(self.activity_lines)

    activity_lines = fields.One2many('op.activity',
                                     'progression_id',
                                     string='Progression Activities')
    total_activity = fields.Integer('Total Activity',
                                    compute="_compute_total_activity",
                                    store=True)
