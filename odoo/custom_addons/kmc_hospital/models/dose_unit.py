from odoo import api, fields, models, _


class HospitalDoseUnit(models.Model):
    _name = 'hospital.dose.unit'
    _description = 'Hospital Dose Unit'

    name = fields.Char(string="Unit", required=True)
    description = fields.Char(string="Description")
