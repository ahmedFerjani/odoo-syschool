# -*- coding: utf-8 -*-
from odoo import http

# class Syschool(http.Controller):
#     @http.route('/syschool/syschool/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/syschool/syschool/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('syschool.listing', {
#             'root': '/syschool/syschool',
#             'objects': http.request.env['syschool.syschool'].search([]),
#         })

#     @http.route('/syschool/syschool/objects/<model("syschool.syschool"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('syschool.object', {
#             'object': obj
#         })