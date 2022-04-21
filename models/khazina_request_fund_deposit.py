from odoo import fields, models
from datetime import datetime,date
from odoo import models, fields, api
from odoo.addons.base.models.assetsbundle import AssetsBundle, JavascriptAsset, CompileError
from collections import OrderedDict
from subprocess import Popen, PIPE
from odoo.tools import misc
import logging
_logger = logging.getLogger(__name__)


class RequestFundDeposit(models.Model):
    _name = "khazina.request_fund_deposit"
    _description = "Khazina Request Fund Deposit"
    date = fields.Date(string='بتاريخ اليوم',default=date.today().strftime('%Y-%m-%d'))
    time = fields.Char(string='ساعة اليوم',default=datetime.now().strftime("%H:%M:%S"))
    recodnumber =fields.Integer(string= 'رقم المحضر',compute='_get_record_id')
    recodreference =fields.Char(string= 'رقم المرجع',compute='_get_reference_number')
    record_editor_name =fields.Many2one('res.users',' اسم و لقب المحرر', default=lambda self: self.env.user)
    
    record_editor_position =fields.Char(string= 'منصب محرر المحضر')
    amount_number=fields.Integer(string= 'المبلغ المعاين با الأرقام')
    amount_letters=fields.Char(string= 'المبلغ المعاين بالحروف')
    signature = fields.Binary(string=' ختم و توقيع المسؤول التجاري')
    secretary_treasury_signature= fields.Binary(string=' ختم و توقيع أمين الخزينة')
    state=fields.Selection([('request','طلب'),('order','أمر'),('done','تم التنفيد')])
    note = fields.Html('Notes')



    def _get_record_id(self):
        self.recodnumber=self.env['khazina.request_fund_deposit'].search([])[-1].id
        

    def _get_reference_number(self):
        self.recodreference=str(self.env['khazina.request_fund_deposit'].search([])[-1].id)+"123"


    def do_clear_done():
        print('yeh yeh')    


    # @api.onchange('state')
    # def _all_country_checked(self):
    #    if (self.all_country=='request'):
    #       self.note.visi
    #    else:           
    #        self.is_show_country = True   



    