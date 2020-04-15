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


class OpenEduCatWebController(http.Controller):

    @http.route('/db_register', type='http', auth='user', website=True,
                csrf=False)
    def db_register(self, **post):
        val = {}
        if post and post.get('instance_key'):
            request.env['res.company'].sudo().search([]).write({
                'openeducat_instance_key': post.get('instance_key')
            })
            if not request.env['res.config.settings']. \
                    request_verify_instance_controller(
                        post.get('instance_key')):
                val.update({'invalid_instance': True})
            else:
                val.update({'hash_allow': True})
        if post and post.get('instance_hash_key'):
            request.env['res.company'].sudo().search([]).write({
                'openeducat_instance_hash_key': post.get('instance_hash_key')
            })
            if request.env['res.config.settings'].request_verify_hash(
                    post.get('instance_hash_key')):
                return request.redirect('/web')
            else:
                val.update({'invalid_hash': True, 'hash_allow': True})
        return request.render("openeducat_web.db_registration", val)
