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
    _name = "op.placement.cell"
    _inherit = ["mail.thread",
                'website.seo.metadata',
                'website.published.multi.mixin']
    _description = "Placement cell team"

    name = fields.Char('Placement Cell Team', required=True,
                       track_visibility='always')
    user_id = fields.Many2one('res.users', string='Team Leader',
                              required=True,
                              track_visibility='always')
    member_ids = fields.One2many('res.users', 'placement_team_id',
                                 string='Channel Members',
                                 track_visibility='always')
    color = fields.Integer("Color Index", default=0)
    department_id = fields.Many2one('op.department', 'Department',
                                    default=lambda self:
                                    self.env.user.dept_id.id)
    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id)
    active = fields.Boolean(default=True)
