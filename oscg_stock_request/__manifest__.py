# -*- coding: utf-8 -*-

{
    'name': "Stock Request",

    'description': """
        Enable to create request for stock purchase from your branch companies or retail shops etc. 
    """,
    'author': "OSCG",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock_request', 'stock_request_kanban', 'stock_request_purchase'],

    # always loaded
    'data': [
    ],
    'summary': "stock purchase request from branch companies or retail shops",
    'images': ['static/description/icon.png'],
    'license': 'OPL-1',
    'currency': 'EUR',
    'price': 30,
    'support': 'sales@oscg.biz',
    'application':True,
}