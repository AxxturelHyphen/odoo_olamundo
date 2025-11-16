from odoo import models, fields

class Olamundo(models.Model):
    _name = 'odoo_olamundo.olamundo'
    _description = 'Modelo Ola Mundo'

    name = fields.Char(string="Título")
    descripcion = fields.Text(string="Descripción")
