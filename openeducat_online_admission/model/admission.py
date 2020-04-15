# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields


class OpAdmission(models.Model):
    _inherit = "op.admission"

    state = fields.Selection(selection_add=[
        ('draft', 'Draft'), ('online', 'Online Admission'),
        ('submit', 'Submitted'), ('confirm', 'Confirmed'),
        ('admission', 'Admission Confirm'), ('reject', 'Rejected'),
        ('pending', 'Pending'), ('cancel', 'Cancelled'), ('done', 'Done')],
        default='draft', track_visibility='onchange')
    order_id = fields.Many2one('sale.order', 'Registration Fees Ref')
    application = fields.Char(selection_add=[('self', 'Delf'), ('other', 'Other')])
