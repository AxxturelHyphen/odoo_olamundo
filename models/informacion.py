from odoo import models, fields

class Informacion(models.Model):
    _name = 'odoo_olamundo.informacion'
    _description = 'Información'

    name = fields.Char(string="Título")
    descripcion = fields.Text(string="Descripción")
    autorizado = fields.Boolean(string="Autorizado")
    sexo_traducido = fields.Char(string="Sexo")
    alto_en_cms = fields.Integer(string="Alto en cms")
    ancho_en_cms = fields.Integer(string="Ancho en cms")
    longo_en_cms = fields.Integer(string="Largo en cms")
    peso = fields.Float(string="Peso")

    foto = fields.Binary(string="Foto")