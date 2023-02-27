from odoo import models, fields, api, _


class HospitalDiagnosticHypothesis(models.Model):
    _name = 'hospital.diagnostic_hypothesis'
    _description = 'hospital diagnostic hypothesis'
    _rec_name = 'diagnostic_pathology_id'

    diagnostic_pathology_id = fields.Many2one('hospital.pathology', 'Procedure')
    patient_ovulation_id = fields.Many2one('hospital.patient.ovulation', 'Patient Ovulation')
    comments = fields.Char('Comments')
