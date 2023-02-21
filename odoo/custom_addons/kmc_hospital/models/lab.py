from odoo import api, fields, models, _
from datetime import date, datetime


class HospitalLab(models.Model):
    _name = 'hospital.lab'
    _description = 'Hospital Lab'

    name = fields.Char('ID')
    test_id = fields.Many2one('hospital.test_type', 'Test Type', required=True)
    date_analysis = fields.Datetime('Date of the Analysis', default=datetime.now())
    patient_id = fields.Many2one('hospital.patient', 'Patient', required=True)
    date_requested = fields.Datetime('Date requested', default=datetime.now())
    hospital_lab_physician_id = fields.Many2one('hospital.physician', 'Pathologist')
    requestor_physician_id = fields.Many2one('hospital.physician', 'Physician', required=True)
    criteria_ids = fields.One2many('hospital_test.criteria', 'hospital_lab_id', 'Criteria')
    results = fields.Text('Results')
    diagnosis = fields.Text('Diagnosis')
    is_invoiced = fields.Boolean(copy=False, default=False)
