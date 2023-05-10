import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-e-commerce",
    description="Meta package for oca-e-commerce Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-website_sale_hide_price>=16.0dev,<16.1dev',
        'odoo-addon-website_sale_product_attribute_value_filter_existing>=16.0dev,<16.1dev',
        'odoo-addon-website_sale_product_reference_displayed>=16.0dev,<16.1dev',
        'odoo-addon-website_sale_stock_available>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
