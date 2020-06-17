# -*- coding: utf-8 -*-

from odoo import models, fields, api


class partner_extended(models.Model):
    _inherit = 'res.partner'
    #_description = 'partner extended'
    
    
    is_customer = fields.Boolean(string="Is customer")
    is_vendor = fields.Boolean(string="Is vendor")
    
    l10n_mx_type_of_operation = fields.Selection([
        ('03', ' 03 - Provision of Professional Services'),
        ('04', ' 04 - Proveedor Nacional'),
        ('05', ' 05 - Proveedor Extranjero'),
        ('06', ' 06 - Renting of buildings'),
        ('85', ' 85 - Others')],
        help='Indicate the operations type that makes this supplier. Is the '
        'second column in DIOT report')
    