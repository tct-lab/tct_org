# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tct_organization(models.Model):
    _name = 'tct_organization.tct_organization'

    name = fields.Char()

    description = fields.Text()

    _sql_constraints = [('name_unique', 'UNIQUE(name)', 'name should be unique')]

    @api.multi
    def open_member_view(self):
        self.ensure_one()
        return {
            'name': 'tct members',
            'view_mode': 'tree,form',
            'view_type': 'form',
            'res_model': 'res.users',

            'type': 'ir.actions.act_window',

            'target': 'current',

        }




class tct_members(models.Model):
    _name = 'tct_members'

    name = fields.Char()
