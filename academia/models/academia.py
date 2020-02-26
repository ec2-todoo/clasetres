# -*- coding: utf-8 -*-

from odoo import models, fields


class academia(models.Model):
     _name = 'academia.alumnos'
     _description = 'Tabla de alumnos'

     name = fields.Char()
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text()
    
state = fields.Selection(selection=[('draft', 'New'),('approve', 'Approved'),('confirm', 'Confirmed'),('cancel', 'Cancelled'),('done', 'Done'),], string='State', default='draft')

select = fields.Selection(selection=[('a', 'A')])
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
