from odoo import api, fields, models, _


class HospitalRoundingProcedure(models.Model):
    _name = 'hospital.rounding_procedure'
    _description = 'Hospital Rounding Procedure'

    notes = fields.Text(string="Notes")
    hospital_patient_rounding_procedure_id = fields.Many2one('hospital.patient.rounding', string="Vaccines")
