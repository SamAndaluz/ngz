# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = "res.company"

    openeducat_core_onboard_panel = fields.Selection(
        [('not_done', "Not done"),
         ('just_done', "Just done"),
         ('done', "Done"),
         ('closed', "Closed")],
        string="State of the onboarding core layout step",
        default='not_done')
    onboarding_course_layout_state = fields.Selection(
        [('not_done', "Not done"),
         ('just_done', "Just done"),
         ('done', "Done"),
         ('closed', "Closed")],
        string="State of the onboarding course layout step",
        default='not_done')
    onboarding_batch_layout_state = fields.Selection(
        [('not_done', "Not done"),
         ('just_done', "Just done"),
         ('done', "Done"),
         ('closed', "Closed")],
        string="State of the onboarding batch layout step",
        default='not_done')
    onboarding_subject_layout_state = fields.Selection(
        [('not_done', "Not done"),
         ('just_done', "Just done"),
         ('done', "Done"),
         ('closed', "Closed")],
        string="State of the onboarding subject layout step",
        default='not_done')

    @api.model
    def action_close_core_onboarding(self):
        """ Mark the onboarding panel as closed. """
        self.env.user.company_id.openeducat_core_onboard_panel = 'closed'

    # course layout starts##

    @api.model
    def action_onboarding_course_layout(self):
        """ Onboarding step for the quotation layout. """
        action = self.env.ref(
            'openeducat_core_enterprise.'
            'action_onboarding_course_layout').read()[0]
        return action

    # batch layout starts#

    @api.model
    def action_onboarding_batch_layout(self):
        """ Onboarding step for the quotation layout. """
        action = self.env.ref(
            'openeducat_core_enterprise.'
            'action_onboarding_batch_layout').read()[0]
        return action

    # subject layout starts##

    @api.model
    def action_onboarding_subject_layout(self):
        """ Onboarding step for the quotation layout. """
        action = self.env.ref(
            'openeducat_core_enterprise.'
            'action_onboarding_subject_layout').read()[0]
        return action

    def update_core_onboarding_state(self):
        """ This method is called on the controller rendering
         method and ensures that the animations
            are displayed only one time. """
        steps = [
            'onboarding_course_layout_state',
            'onboarding_batch_layout_state',
            'onboarding_subject_layout_state'
        ]
        return self.get_and_update_onbarding_state(
            'openeducat_core_onboard_panel', steps)
