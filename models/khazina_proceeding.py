from odoo import fields, models



class Proceedings(models.Model):
 _name = "khazina.proceeding"
 _description = "Khazina Proceedings"
 name = fields.Char("Title", required=True)
 isbn = fields.Char("ISBN")
 active = fields.Boolean("Active?", default=True)
 date_published = fields.Date()
 image = fields.Binary("Cover")
 publisher_id = fields.Many2one("res.partner",string="Publisher")
 author_ids = fields.Many2many("res.partner",string="Authors")




 def button_check_isbn(self):
    print("Hi  Hi HI")