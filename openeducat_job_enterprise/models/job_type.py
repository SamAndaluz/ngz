# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields


class OpJobType(models.Model):
    _name = "op.job.type"
    _description = "Job Type Creation"

    name = fields.Char('Employment Type', required=True)
    code = fields.Char('Code', size=64, required=True)
