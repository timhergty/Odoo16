from odoo import models, fields, api, _


class HospitalDirections(models.Model):
    _name = 'hospital.directions'
    _description = 'Hospital Directions'
    _rec_name = 'hospital_directions_pathology_id'

    hospital_directions_pathology_id = fields.Many2one('hospital.pathology', 'Procedure')
    patient_ovulation_id = fields.Many2one('hospital.patient.ovulation', 'Patient Ovulation')
    comments = fields.Char('Comments')
