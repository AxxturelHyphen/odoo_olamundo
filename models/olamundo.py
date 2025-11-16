from odoo import models, fields


class OlaMundo(models.Model):
    _name = "odoo_olamundo.olamundo"      # nombre técnico del modelo
    _description = "Ola Mundo (ejemplo)"

    # Primer campo de la tabla:
    name = fields.Char(string="Ola Mundo:")
