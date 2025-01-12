{
    'name': 'Product Category Margin',
    'version': '1.0',
    'author': 'Izsó Péter',
    'category': 'Product',
    'summary': 'Adds minimum margin rate functionality to product categories.',
    'description': """
    This module adds a minimum margin rate field to product categories.
    """,
    'depends': ['product'],
    'data': [
        'views/product_category_views.xml',
    ],
    'installable': True,
    'application': False,
}
