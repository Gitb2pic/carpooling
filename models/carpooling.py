#-*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

 
class Carpooling(models.Model):
    _name = "carpooling.carpooling"
    _description = """
        this is a model for carpooling
    """
    _order = 'sequence asc, id desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True)
    taken_seats = fields.Integer(string="Taken Seats", tracking=True)
    departure_time = fields.Float(string='Departure time', tracking=True)
    departure_date = fields.Date(string='Departure date', tracking=True)
    departure_city = fields.Char(string="departure city", tracking=True)
    destination_city = fields.Char(string="Destination city", tracking=True)
    note = fields.Text('Note')
    resume = fields.Html('resume')
    image = fields.Binary(string="image")
    is_free = fields.Boolean('Est disponible')
    states = [('new', 'New'), ('available', 'Has seats available'), ('full', 'Full')]
    state = fields.Selection(selection=states, default='new')
    company_currency = fields.Many2one('res.currency', string='currency', compute="_compute_company_currency")
    amount_per_km = fields.Monetary(string="Amount per km", currency_field="company_currency", tracking=True)
    car_id = fields.Many2one('carpooling.car', string="Car", required=True)
    km = fields.Float(string="Distance", required=True, tracking=True)
    cost = fields.Monetary(string="cost", currency_field="company_currency", compute="_calcul_cost", store=True, tracking=True)
    sequence = fields.Integer()
    @api.constrains('km')
    def _check_km(self):
        for rec in self:
            if rec.km < 0:
                raise ValidationError("Tu ne peut pas avoir des distance négative.")
       
    @api.depends("km", "amount_per_km")
    def _calcul_cost(self):
        for rec in self:
            rec.cost = rec.amount_per_km * rec.km

    def _compute_company_currency(self):
        for rec in self:
            rec.company_currency = self.env.company.currency_id.id
        
    def increment_departure_time(self):
        for rec in self:
            rec.departure_time = rec.departure_time + 1

    def _run_cron(self):
        for carpool in self.search([]):
            carpool.taken_seats = carpool.taken_seats + 1