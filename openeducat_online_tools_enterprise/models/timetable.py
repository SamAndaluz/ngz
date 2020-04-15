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

    op_session_id = fields.Many2one('op.session', string="Session")
    mpw = fields.Char("Moderator Password")
    meeting_url = fields.Char("URL")
    online_meeting = fields.Boolean("Online Meeting", copy=False)


class Attendee(models.Model):
    _inherit = 'calendar.attendee'

    attendee_meeting_url = fields.Char('URL')
    apw = fields.Char("Attendee Password")


class OpSession(models.Model):
    _inherit = 'op.session'

    def _get_meetings(self):
        for record in self:
            record.meeting_count = self.env['calendar.event'].search_count(
                [('op_session_id', 'in', self.ids)])

    meeting_count = fields.Integer(string='Meeting Count',
                                   compute='_get_meetings', readonly=True)

    def action_view_online_meetings(self):

        event_ids = self.env['calendar.event'].search(
            [('op_session_id', 'in', self.ids)])

        action = self.env.ref('calendar.action_calendar_event').read()[0]

        osc_ids = self.env['op.student.course'].search((
            ['course_id', '=', self.course_id.id],
            ['batch_id', '=', self.batch_id.id],
        ))
        student_partner_ids = [osc.student_id.partner_id.id for osc in osc_ids]
        if len(event_ids) >= 1:
            action['domain'] = [('op_session_id', 'in', self.ids)]
        # elif len(event_ids) == 1:
        else:
            form_view = [
                (self.env.ref('calendar.view_calendar_event_form').id, 'form')]
            if 'views' in action:
                action['views'] = form_view + [
                    (state, view) for state, view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = event_ids.id

        context = {
        }
        if len(self) == 1:
            partner_ids = student_partner_ids or []
            partner = self.env.user.partner_id
            partner_ids.append(partner.id)
            for rec in self:
                for rec1 in rec.user_ids:
                    partner_ids.append(rec1.partner_id.id)
            context.update({
                'default_partner_id': self.faculty_id.partner_id.id,
                'default_name': self.name,
                'default_start': self.start_datetime,
                'default_stop': self.end_datetime,
                'default_partner_ids': [[6, 0, list(set(partner_ids))]],
                'default_user_id': self.faculty_id.user_id.id,
                'default_op_session_id': self.id
            })

        action['context'] = context
        return action

    def create_online_meeting(self):
        action = self.env.ref('calendar.'
                              'action_calendar_event').read()[0]
        action['domain'] = [('op_session_id', 'in', self.ids)]
        return action
