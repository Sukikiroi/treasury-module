from odoo import fields, models
from datetime import datetime,date


class RequestFundDeposit(models.Model):
    _name = "khazina.request_fund_deposit"
    _description = "Khazina Request Fund Deposit"
    date = fields.Date(string='بتاريخ اليوم',default=date.today().strftime('%Y-%m-%d'))
    time = fields.Char(string='ساعة اليوم',default=datetime.now().strftime("%H:%M:%S"))
    recodnumber =fields.Integer(string= 'رقم المحضر',compute='_get_record_id')
    recodreference =fields.Char(string= 'رقم المرجع')
    record_editor_name =fields.Char(string= ' لقب محرر المحضر')
    record_editor_last_name =fields.Char(string= 'اسم محرر المحضر')
    record_editor_position =fields.Char(string= 'منصب محرر المحضر')
    amount_number=fields.Integer(string= 'المبلغ المعاين باالحروف')
    amount_letters=fields.Char(string= 'المبلغ المعاين بالحروف')
    signature = fields.Binary(string=' ختم و توقيع المسؤول التجاري')
    secretary_treasury_signature= fields.Binary(string=' ختم و توقيع أمين الخزينة')
    state=fields.Selection([('request','طلب'),('order','أمر'),('testimonial','اشهاد')])




    def _get_record_id(self):
        self.recodnumber=self.env['khazina.request_fund_deposit'].search([])[-1].id

    def do_clear_done():
        print('yeh yeh')    