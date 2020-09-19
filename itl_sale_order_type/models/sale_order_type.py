# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrderTypology(models.Model):
    _inherit = "sale.order.type"
    
    approval_request = fields.Boolean(string="Approval request", default=False)