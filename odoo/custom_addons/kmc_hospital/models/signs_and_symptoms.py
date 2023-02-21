from odoo import models, fields, api, _


class HospitalSignsAndSymptoms(models.Model):
    _name = 'hospital.signs.and.symptoms'
    _description = 'Hospital Signs and Symptoms'
    _rec_name = 'pathology_id'

    patient_evaluation_id = fields.Many2one('hospital.patient.evaluation', 'Patient Evaluation')
    pathology_id = fields.Many2one('hospital.pathology', 'Sign or Symptom')
    sign_or_symptom = fields.Selection([
        ('sign', 'Sign'),
        ('symptom', 'Symptom'),
    ], string='Subjective / Objective')
    comments = fields.Char('Comments')
