# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from odoo import models, api, fields, _
from odoo.exceptions import AccessError, ValidationError
from random import choice

from . import bbb_api as bbb


class BbbMeeting(models.TransientModel):
    _name = "bbb.meeting"
    _description = "BBb Meeting"

    name = fields.Char("Name / Subject")
    user_id = fields.Many2one('res.users', 'User',
                              default=lambda self: self._uid)
    apw = fields.Char("Attendee password", default=lambda self: self.create_apw())
    mpw = fields.Char("Moderator password", default=lambda self: self.create_mpw())
    welcome_str = fields.Char("Welcome String", help="welcome message to be \
                              displayed when a user logs in to the meeting")
    session_id = fields.Many2one("op.session", 'Session')
    invite_via_email = fields.Boolean('Invite Via Email')
    meeting_id = fields.Many2one('calendar.event', 'Meeting')

    def create_mpw(self):
        size = 6
        values = '0123456789'
        p = ''
        p = p.join([choice(values) for i in range(size)])
        return p

    def create_apw(self):
        size = 6
        values = '0123456789'
        p = ''
        p = p.join([choice(values) for i in range(size)])
        return p

    @api.model
    def default_get(self, fields):
        res = super(BbbMeeting, self).default_get(fields)
        context = dict(self.env.context)
        active_id = context.get('active_id', False)
        calender = self.env['calendar.event'].browse(active_id)
        res.update({
            'meeting_id': active_id,
            'name': calender.name,
            'welcome_str': "Welcome to " + calender.name,
            'invite_via_email': True,
        })
        return res

    def create_meeting(self):
        res_param = self.env['ir.config_parameter']
        for record in self:
            url = res_param.search([
                ('key', '=', 'bigbluebutton.url')])
            salt = res_param.search([
                ('key', '=', 'bigbluebutton.secret')])
            if not url or not salt:
                raise AccessError(
                    _('Please Configure BigBlueButton Credentials'))
            url = url.value
            salt = salt.value
            base_url = res_param.search([
                ('key', '=', 'web.base.url')])
            if not base_url:
                raise AccessError(
                    _('Please Configure URL in System Parameters'))
            base_url = base_url.value
            apw = record.apw
            mpw = record.mpw
            meeting = bbb.createMeeting(
                record.user_id.name, record.id, record.welcome_str, mpw,
                apw, salt, url, base_url)
            if meeting:
                record.meeting_id.write({
                    'meeting_name': meeting['meetingID'],
                    'apw': apw,
                    'mpw': mpw,
                    'salt': salt,
                    'meeting_url': url,
                    'online_meeting': True,
                })
                for attendee in self.meeting_id.attendee_ids:
                    join_url = bbb.joinURL(
                        record.meeting_id.meeting_name, attendee.partner_id.name,
                        record.meeting_id.apw,
                        record.meeting_id.salt,
                        record.meeting_id.meeting_url)
                    attendee.write({
                        'attendee_meeting_url': join_url,
                        'apw': apw,
                    })
                if record.invite_via_email is True:
                    record.meeting_id.action_sendmail()
            return True
        else:
            raise ValidationError("Unable to reach server")
