# -*- coding: utf-8 -*-
from odoo import http
import logging
_logger = logging.getLogger(__name__)

class AaaApiDevelop(http.Controller):
    @http.route('/aaa/api/develop', auth='public', website=False, csrf=False, type='http', methods=['Get'])
    def index(self, **kw):
        _logger.info(kw)
        sum = int(kw['a']) + int(kw['b'])
        sub = int(kw['a']) - int(kw['b'])
        mul = int(kw['a']) * int(kw['b'])
        div = int(kw['a']) / int(kw['b'])
        return "Sum: %s \n Sub: %s \n Mul: %s\n  Div: %s" % (sum, sub, mul, div)

