# -*- coding: utf-8 -*-

from odoo import models, fields

#class academiaEtiqueta(models.Model):
 #   _name = 'academia.tags'
 #   _description ='Academia Tags'
 #   name = fields.Char(string='Name')

class academia(models.Model):
    _name = 'academia.alumnos'
    _description = 'Tabla de alumnos'
    
    name = fields.Char(string='Nombre',  required=True, 
                        index=True, help='Ingres el nombre de alumno.',
                          readonly=True, states={'approve': [('readonly', False)]})
    value = fields.Integer(required=True)
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection(selection=[('draft', 'New'),
                                        ('approve', 'Approved'),
                                        ('confirm', 'Confirmed'),
                                        ('cancel', 'Cancelled'),
                                        ('done', 'Done'),],
                             string='State', default='draft')
    
    location_id = fields.Many2one(comodel_name='res.partner', ondelete='restrict',readonly=True)
    #, states={'draft': [('readonly', False)], 'approve': [('readonly', False)]}
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
