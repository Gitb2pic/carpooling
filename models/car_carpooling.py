from odoo import models, fields

class CarCarpooling(models.Model):
    _name = "carpooling.car"
    _description = """Information car"""

    name = fields.Char(string="Marque", required=True)
    display_seat = fields.Integer(string="Nombre de places disponible", required=True)
    traject_id = fields.One2many('carpooling.carpooling', 'car_id', string="Traject Programmé")
