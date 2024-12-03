from odoo import models, fields, api

class CustomReportConfiguration(models.Model):
    _inherit = 'res.company'

    report_header_text = fields.Text(
        string='Report Header Text',
        help='Custom text to be displayed in document headers'
    )

    def _get_document_type_name(self, document):
        """Dynamic document type naming"""
        type_mappings = {
            'sale.order': 'Sales Quotation',
            'account.move': self._get_invoice_type_name(document)
        }
        return type_mappings.get(document._name, 'Document')

    def _get_invoice_type_name(self, invoice):
        """Determine invoice type name"""
        if invoice.move_type == 'out_invoice':
            return 'Customer Invoice'
        elif invoice.move_type == 'in_invoice':
            return 'Vendor Bill'
        elif invoice.move_type == 'out_refund':
            return 'Customer Credit Note'
        elif invoice.move_type == 'in_refund':
            return 'Vendor Credit Note'
        return 'Invoice'