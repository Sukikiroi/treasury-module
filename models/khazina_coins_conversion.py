from odoo import fields, models



class CoinsConversion(models.Model):
 _name = "khazina.coins_conversion"
 _description = "Khazina Coins Conversion"
 name = fields.Char("Title", required=True)
 isbn = fields.Char("ISBN")
 active = fields.Boolean("Active?", default=True)
 date_published = fields.Date()




 