from odoo import fields, models



class Loan(models.Model):
    _name = "khazina.request_loan"
    _description = "Khazina Loan"
    name = fields.Char("Title", required=True)
    isbn = fields.Char("ISBN")
    active = fields.Boolean("Active?", default=True)
    date_published = fields.Date()
    state= fields.Char()



    def button_done():
        print('state')