from odoo import models, fields, api

class ProductCategory(models.Model):
    _inherit = 'product.category'

    min_margin_rate = fields.Float(
        string='Minimum Margin Rate (%)',
        help='The minimum acceptable margin rate for this product category.',
    )

    def recalculate_margin_difference(self):
        """ This method updates margin fields for all products in this category. """
        products = self.env['product.product'].search([('categ_id', '=', self.id)])
        for product in products:
            product._compute_margin_difference()  # Assuming you have this method defined in ProductProduct model
