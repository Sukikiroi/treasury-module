from odoo import fields, models



class Feed(models.Model):
    _name = "khazina.request_feed"
    _description = "Khazina Feed"
    name = fields.Char("Title", required=True)
    isbn = fields.Char("ISBN")
    active = fields.Boolean("Active?", default=True)
    date_published = fields.Date()