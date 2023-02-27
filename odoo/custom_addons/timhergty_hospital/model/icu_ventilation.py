from odoo import models, fields, api, _
from datetime import date, datetime


class HospitalIcuVentilation(models.Model):
    _name = 'hospital.icu.ventilation'
    _description = 'Hospital Icu ventilation'
    _rec_name = 'ventilation'

    current_mv = fields.Boolean(string="Current", required=True, default=True)
    mv_start = fields.Datetime(string="From", required=True)
    mv_end = fields.Datetime(string="To", required=True)
    mv_period = fields.Char(string="Duration", size=128, required=True)
    ventilation = fields.Selection(
        [('none', 'None - Maintains Own'), ('nppv', 'Non-Invasive Psitive Pressure'), ('ett', 'ETT'),
         ('tracheostomy', 'Tracheostomy')], string="Type")
    remarks = fields.Char(string="Remarks")
