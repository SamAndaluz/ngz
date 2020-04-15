# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright(C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################
from odoo import models, fields


class Meeting(models.Model):
    _inherit = 'calendar.event'

    salt = fields.Char("Salt")
    apw = fields.Char("Attendee Password")
    meeting_name = fields.Char("Meeting ID")
