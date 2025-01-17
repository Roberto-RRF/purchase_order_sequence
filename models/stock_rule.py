from odoo import api, fields, models

class StockRule(models.Model):
    _inherit = 'stock.rule'


    def _prepare_purchase_order(self, company_id, origins, values):
        # Call the super method to get the original dictionary
        vals = super(StockRule, self)._prepare_purchase_order(company_id, origins, values)
        vals['tipo_de_orden'] = 'indirectos'
        return vals