from odoo import models, fields
from odoo. exceptions import ValidationError

class CarpoolingWizard(models.TranscienModel):
    _name = "carpooling.wizard"
    _description = "Carpooling Wizard"

    departure_date = fields.Date(string='Departure date')
    departure_city = fields.Char(string="departure city")
    destination_city = fields.Char(string="Destination city")

    def search_trip(self):
        carpool = self.env['carpooling.carpooling'].search([
            ('departure_date', '=', self.departure_date),
            ('departure_city', '=', self.departure_city),
            ('destination_city', '=', self.destination_city)
        ])
        if carpool:
            raise ValidationError(f"Destination trouve à l'id {carpool.id}")
        else:
             raise ValidationError(f"Pas destination trouve")