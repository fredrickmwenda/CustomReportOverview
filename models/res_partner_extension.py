from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    kra_pin = fields.Char(string='KRA PIN', help='Kenya Revenue Authority Personal Identification Number')
    mobile = fields.Char(string='Mobile Number', help='Customer Mobile Number')