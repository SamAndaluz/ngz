# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields


class OpLibraryCardType(models.Model):
    _inherit = "op.library.card.type"

    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id)

    def action_onboarding_library_card_type_layout(self):
        self.env.user.company_id.onboarding_library_card_type_layout_state =\
            'done'


class OpLibraryCard(models.Model):
    _inherit = "op.library.card"

    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id)

    def action_onboarding_library_card_layout(self):
        self.env.user.company_id.onboarding_library_card_layout_state =\
            'done'
