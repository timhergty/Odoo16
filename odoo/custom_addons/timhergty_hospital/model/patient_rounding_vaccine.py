from odoo import api, fields, models, _
from datetime import date, datetime


class HospitalPatientRoundingVaccine(models.Model):
    _name = 'hospital.patient.rounding.vaccine'
    _description = 'Hospital Patient Rounding Vaccine'

    vaccine_id = fields.Many2one('product.product', string="Vaccines", required=True)
    quantity = fields.Integer(string="Quantity")
    lot_id = fields.Many2one('stock.production.lot', string='Lot', required=True)
    dose = fields.Integer(string="Dose")
    next_dose_date = fields.Datetime(string="Next Dose")
    short_comment = fields.Char(string='Comment')
    hospital_patient_rounding_vaccine_id = fields.Many2one('hospital.patient.rounding', string="Vaccines")
