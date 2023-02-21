from odoo import api, fields, models, _


class HospitalMedicationDosage(models.Model):
    _name = 'hospital.medication.dosage'
    _description = 'Hospital Medication Dosage'

    name = fields.Char(string="Frequency", required=True)
    abbreviation = fields.Char(string="Abbreviation")
    code = fields.Char(string="Code")
