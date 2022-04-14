from odoo import fields, models



class TestimonialCoinsConversion(models.Model):
    _name = "khazina.testimonial_coins_conversion"
    _description = "Khazina Testimonial Coins Conversion"
    name = fields.Char("Title", required=True)
    isbn = fields.Char("ISBN")
    active = fields.Boolean("Active?", default=True)
    date_published = fields.Date()