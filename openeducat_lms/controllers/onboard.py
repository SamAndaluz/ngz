# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.http import request


class LmsOnboardingController(http.Controller):

    @http.route('/openeducat_lms/'
                'openeducat_lms_onboarding_panel',
                auth='user', type='json')
    def openeducat_lms_onboarding_panel(self):
        """ Returns the `banner` for the sale onboarding panel.
            It can be empty if the user has closed it or if he doesn't have
            the permission to see it. """

        company = request.env.user.company_id
        if not request.env.user._is_admin() or \
           company.lms_onboard_panel == 'closed':
            return {}

        return {
            'html': request.env.ref(
                'openeducat_lms.'
                'openeducat_lms_onboarding_panel').render({
                    'company': company,
                    'state': company.update_lms_onboarding_state()
                })

        }
