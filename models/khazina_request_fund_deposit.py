from odoo import fields, models



class RequestFundDeposit(models.Model):
    _name = "khazina.request_fund_deposit"
    _description = "Khazina Request Fund Deposit"
    name = fields.Char("Title", required=True)
    isbn = fields.Char("ISBN")
    active = fields.Boolean("Active?", default=True)
    date_published = fields.Date()