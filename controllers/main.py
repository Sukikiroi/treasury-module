# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class Main(http.Controller):
      @http.route('/khazina/todo/', auth='public')
      def index(self, **kw):
        context = {
            'session_info': json.dumps(request.env['ir.http'].session_info())
        }
        return request.render('khazina.fund_catalog', qcontext=context)