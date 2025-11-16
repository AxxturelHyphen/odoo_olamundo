from odoo import models, fields

class Informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Información básica'

    name = fields.Char(string="Nombre")
    descripcion = fields.Text()
    autorizado = fields.Boolean()
    sexo_traducido = fields.Char()
    alto_en_cms = fields.Integer()
    longo_en_cms = fields.Integer()
    ancho_en_cms = fields.Integer()
    peso = fields.Float()
