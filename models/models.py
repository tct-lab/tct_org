# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tct_organization(models.Model):
    _name = 'tct_organization.tct_organization'

    name = fields.Char()

    description = fields.Text()

    _sql_constraints = [('name_unique', 'UNIQUE(name)', 'name should be unique')]





class tct_members(models.Model):
    _name = 'tct_members'

    name = fields.Char()
