from odoo import models, fields, api, _


class HospitalSecondaryCondition(models.Model):
    _name = 'hospital.secondary_condition'
    _description = 'Hospital Secondary Condition'
    _rec_name = 'pathology_id'

    patient_ovulation_id = fields.Many2one('hospital.patient.ovulation', 'Patient Ovulation')
    pathology_id = fields.Many2one('hospital.pathology', 'Pathology')
    comments = fields.Char('Comments')
