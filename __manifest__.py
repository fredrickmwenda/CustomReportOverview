{
    'name': 'Custom Document Reports',
    'version': '1.0',
    'category': 'Reporting',
    'summary': 'Customized Quotation and Invoice Reports',
    'description': """
    Enhanced reporting layout for:
    - Sales Quotations
    - Customer Invoices
    - Vendor Bills
    """,
    'author': 'Your Company',
    'depends': [
        'base', 
        'web', 
        'sale', 
        'account'
    ],
    'data': [
        'views/report_external_layout.xml',
        'views/sale_order_report_templates.xml',
        'views/account_move_report_templates.xml'
         'views/res_partner_views.xml',  # Add this line
    ],
    'assets': {
        'web.report_assets_common': [
            '/custom_document_reports/static/src/css/custom_report.css',
        ],
    },
    'installable': True,
    'application': False,
}