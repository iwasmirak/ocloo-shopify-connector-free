# Copyright 2026 Ocloo
# License OPL-1 (https://www.odoo.com/documentation/19.0/legal/licenses.html)
{
    'name': 'Ocloo Connector for Shopify (Free Trial)',
    'version': '19.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Free trial (25 products, 1 Shopify store, 30 days): two-way sync of products, images, tags, collections, multi-location stock, orders, customers, invoices, payouts and returns, with real-time webhooks.',
    'description': 'Two-way synchronization between Odoo and Shopify: see README.rst and static/description.',
    'author': 'Ocloo',
    'maintainer': 'Ocloo',
    'support': 'contact@ocloo.tech',
    'website': 'https://ocloo.tech',
    'license': 'OPL-1',
    'price': 0.0,
    'currency': 'USD',
    'images': ['static/description/banner.png', 'static/description/icon.png', 'static/description/screenshot_dashboard.png', 'static/description/screenshot_store.png', 'static/description/screenshot_product.png', 'static/description/screenshot_links.png', 'static/description/screenshot_logs.png'],
    'depends': ['sale_stock'],
    'external_dependencies': {'python': ['cryptography']},
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'views/mirak_shopify_store_views.xml',
        'views/mirak_shopify_product_map_views.xml',
        'views/mirak_shopify_log_views.xml',
        'views/product_template_views.xml',
        'views/sale_views.xml',
        'views/dashboard_views.xml',
        'views/menus.xml',
        'views/mirak_shopify_extra_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'mirak_shopify_connector_trial/static/src/dashboard/*',
        ],
    },
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': True,
}
