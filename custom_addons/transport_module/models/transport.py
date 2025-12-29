from datetime import date
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Transport(models.Model):
    _name = 'transport.transport'
    _description = 'Transport Information'

    carrier_id = fields.Many2one('res.partner', string='Daşıyıcı')
    delivery_date = fields.Date(string='Çatdırılma müddəti')
    from_location = fields.Char(string='Haradan')
    to_location = fields.Char(string='Haraya')
    product_id = fields.Many2one('product.product', string='Product')
    transport_mode = fields.Selection(
        [
            ('road', 'Road'),
            ('sea', 'Sea'),
            ('air', 'Air'),
            ('rail', 'Rail')
        ],
        string='Transport Mode'
    )
    incoterm_id = fields.Many2one('account.incoterms', string='Incoterm')

    @api.constrains('from_location', 'to_location')
    def _check_locations(self):
        for rec in self:
            if rec.from_location and rec.to_location:
                if rec.from_location.strip().lower() == rec.to_location.strip().lower():
                    raise ValidationError(
                        "Haradan və Haraya eyni ola bilməz."
                    )

    @api.constrains('delivery_date')
    def _check_delivery_date(self):
        for rec in self:
            if rec.delivery_date and rec.delivery_date < date.today():
                raise ValidationError(
                    "Çatdırılma müddəti keçmiş tarix ola bilməz."
                )