# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields


class OpEvent(models.Model):
    _inherit = "event.event"

    alumni_event_id = fields.Many2one('op.alumni.group', string='Alumni Group')


class Opalumni(models.Model):
    _inherit = "op.alumni.group"

    event_ids = fields.One2many(
        'event.event', 'alumni_event_id', string='Events')
