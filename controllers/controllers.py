# -*- coding: utf-8 -*-
from odoo import http

# class TctOrganization(http.Controller):
#     @http.route('/tct_organization/tct_organization/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tct_organization/tct_organization/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tct_organization.listing', {
#             'root': '/tct_organization/tct_organization',
#             'objects': http.request.env['tct_organization.tct_organization'].search([]),
#         })

#     @http.route('/tct_organization/tct_organization/objects/<model("tct_organization.tct_organization"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tct_organization.object', {
#             'object': obj
#         })