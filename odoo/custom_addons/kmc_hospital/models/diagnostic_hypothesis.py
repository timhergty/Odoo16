from odoo import models, fields, api, _


class HospitalDiagnosticHypothesis(models.Model):
    _name = 'hospital.diagnostic_hypothesis'
    _description = 'Hospital Diagnostic Hypothesis'
    _rec_name = 'diagnostic_pathology_id'

    diagnostic_pathology_id = fields.Many2one('hospital.pathology', 'Procedure')
    patient_evaluation_id = fields.Many2one('hospital.patient.evaluation', 'Patient Evaluation')
    comments = fields.Char('Comments')
