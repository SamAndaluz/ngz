# -*- coding: utf-8 -*-
# Part of OpenEduCat. See LICENSE file for full copyright & licensing details.

##############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech Receptives(<http://www.techreceptives.com>).
#
##############################################################################

import logging

from .test_health_common import TestHealthCommon


class TestHealth(TestHealthCommon):

    def setUp(self):
        super(TestHealth, self).setUp()

    def test_case_health(self):
        types = self.op_health.search([])
        for health in types:
            health.check_height_weight()


class TestHealthLine(TestHealthCommon):

    def setUp(self):
        super(TestHealthLine, self).setUp()

    def test_case_health_line(self):
        types = self.op_health_line.search([])
        for healthline in types:
            logging.info('Date : %s' % healthline.date)
            logging.info('Checkup Detail : %s' % healthline.name)
