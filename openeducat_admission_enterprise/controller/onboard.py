# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo.http import request

from odoo import http


class OnboardingController(http.Controller):
    @http.route(
        '/openeducat_admission_enterprise/openeducat_admission_onboarding',
        auth='user', type='json')
    def openeducat_admission_onboarding(self):
        """ Returns the `banner` for the sale onboarding panel.
            It can be empty if the user has closed it or if he doesn't have
            the permission to see it. """
        company = request.env.user.company_id
        if not request.env.user._is_admin() or \
                company.openeducat_admission_onboard_panel == 'closed':
            return {}
        return {
            'html': request.env.ref(
                'openeducat_admission_enterprise.'
                'openeducat_admission_onboarding_panel').render({
                    'company': company,
                    'state': company.update_admission_onboarding_state()
                })
        }
