# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

import logging
from .test_core_common import TestCoreCommon


class TestComapny(TestCoreCommon):

    def setUp(self):
        super(TestComapny, self).setUp()

    def test_case_1_company(self):
        company = self.res_company.search([])

        logging.info('Details of Core Company')
        logging.info(
            'openeducat_core_onboard_panel : %s :  ' % (
                company.openeducat_core_onboard_panel))
        logging.info('onboarding_course_layout_state : %s :  ' % (
            company.onboarding_course_layout_state))
        logging.info('onboarding_batch_layout_state : %s :  ' % (
            company.onboarding_batch_layout_state))
        logging.info('onboarding_subject_layout_state : %s :  ' % (
            company.onboarding_subject_layout_state))

        company.action_close_core_onboarding()
        company.action_onboarding_course_layout()
        company.action_onboarding_batch_layout()
        company.action_onboarding_subject_layout()
        company.update_core_onboarding_state()


class TestBatch(TestCoreCommon):

    def setUp(self):
        super(TestBatch, self).setUp()

    def test_case_1_batch(self):
        batch = self.op_batch.search([])

        logging.info('Details of Core batch')
        batch.action_onboarding_batch_layout()


class TestCourse(TestCoreCommon):

    def setUp(self):
        super(TestCourse, self).setUp()

    def test_case_1_course(self):
        course = self.op_course.search([])

        logging.info('Details of Core course')
        course.action_onboarding_course_layout()


class TestFaculty(TestCoreCommon):

    def setUp(self):
        super(TestFaculty, self).setUp()

    def test_case_1_faculty(self):
        faculty = self.op_faculty.search([], limit=1)

        logging.info('Details of Core faculty:: %s' % faculty)
        logging.info('  Company      :    Name   ')
        for faculty in faculty:
            logging.info('%s  : %s' % (faculty.company_id, faculty.name))
        faculty.create_employee()

        faculty.get_dashboard_data()


class TestSubject(TestCoreCommon):

    def setUp(self):
        super(TestSubject, self).setUp()

    def test_case_1_subject(self):
        subject = self.op_subject.search([])

        logging.info('Details of Core subject')
        logging.info('  Company      :    Name   ')
        for subject in subject:
            logging.info('%s  : %s' % (subject.company_id, subject.name))
            logging.info('Course  Name : %s :' % (subject.course_id.name))

        subject.action_onboarding_subject_layout()
        subject.create({
            'name': 'new subject',
            'code': 'A',
            'course_id': 1,
            'type': 'theory',
            'subject_type': 'elective',

        })


class TestWizardCore(TestCoreCommon):

    def setUp(self):
        super(TestWizardCore, self).setUp()

    def test_wizard_grant_badge(self):
        wizard = self.wizard_badge.create({
            'student_id': self.env.ref('openeducat_core.op_student_1').id,
            'badge_id': self.env.ref(
                'openeducat_core_enterprise.op_gamification_badge_1').id,
            'comment': 'take it easy',
        })
        wizard.action_grant_badge()
