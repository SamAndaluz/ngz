# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.
#
##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

from logging import info

from .test_scholarship_common import TestScholarshipCommon


class TestScholarship(TestScholarshipCommon):

    def setUp(self):
        super(TestScholarship, self).setUp()

    def test_case_scholarship(self):
        scholarship = self.op_scholarship.search([])
        if not scholarship:
            raise AssertionError(
                'Error in data, please check for scholarship details')
        info('  Details Of Scholarship:.....')
        for record in scholarship:
            info('      Name : %s' % record.name)
            info('      Student : %s' % record.student_id.name)
            info('      Type : %s' % record.type_id.name)
            info('      State : %s' % record.state)
            info('      Company : %s' % record.company_id.name)
            record.act_confirm()
            record.act_reject()


class TestScholarshipType(TestScholarshipCommon):

    def setUp(self):
        super(TestScholarshipType, self).setUp()

    def test_case_scholarship_type(self):
        scholarshiptype = self.op_scholarship_type.search([])
        if not scholarshiptype:
            raise AssertionError(
                'Error in data, please check for scholarship type details')
        info('  Details Of Scholarship Type:.....')
        for record in scholarshiptype:
            info('      Name : %s' % record.name)
            info('      Amount : %s' % record.amount)
            info('      Company : %s' % record.company_id.name)
            record.check_amount()
