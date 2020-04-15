# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class OpScholarshipType(models.Model):
    _name = "op.scholarship.type"
    _description = "Scholarship Type"

    name = fields.Char('Name', size=64, required=True)
    amount = fields.Integer('Amount')
    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.user.company_id)
    active = fields.Boolean(default=True)

    @api.constrains('amount')
    def check_amount(self):
        if self.amount <= 0:
            raise ValidationError(_('Enter proper Amount'))
