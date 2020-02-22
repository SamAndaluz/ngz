# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import http
from odoo.http import request
from odoo.addons.openeducat_alumni_enterprise.controller.main import AlumniWeb


class AlumniBlog(AlumniWeb):

    @http.route()
    def alumni_detail(self, alumni, **kwargs):
        response = super(AlumniBlog, self).alumni_detail(alumni=alumni,
                                                         **kwargs)
        post = request.env["blog.post"]
        blogpost = post.sudo().search([('id', 'in', alumni.blog_post_ids.ids)])
        response.qcontext.update({
            'blogpost': blogpost,
        })
        return response
