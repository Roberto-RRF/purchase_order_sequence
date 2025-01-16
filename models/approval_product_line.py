   
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools.misc import clean_context

class ApprovalProductLine(models.Model):
    _inherit = 'approval.product.line'

    def _get_purchase_order_values(self, vendor):
        vals = super(ApprovalProductLine, self)._get_purchase_order_values(vendor)
        vals['tipo_de_orden'] = 'indirectos'
        return vals

