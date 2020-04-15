# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields


class OpBlogPost(models.Model):
    _inherit = "blog.post"

    alumni_group_id = fields.Many2one('op.alumni.group', string='Alumni Group')


class Opalumni(models.Model):
    _inherit = "op.alumni.group"

    blog_post_ids = fields.One2many(
        'blog.post', 'alumni_group_id', string='Blog')
