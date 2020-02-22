# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################
from odoo.tests import common


class TestLmsBlogCommon(common.SavepointCase):
    def setUp(self):
        super(TestLmsBlogCommon, self).setUp()
        self.op_course = self.env['op.course']
        self.blogs = self.env['blog.blog']
        self.blog_posts = self.env['blog.post']
        self.blog_tags = self.env['blog.blog']
