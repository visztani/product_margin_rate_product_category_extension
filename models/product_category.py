from odoo import models, fields, api

class ProductCategory(models.Model):
    _inherit = 'product.category'

    min_margin_rate = fields.Float(
        string='Minimum Margin Rate (%)',
        help='The minimum acceptable margin rate for this product category.',
    )