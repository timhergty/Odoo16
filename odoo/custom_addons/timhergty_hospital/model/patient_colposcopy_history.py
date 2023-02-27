from odoo import api, fields, models, _
from datetime import date, datetime


class HospitalPatientColposcopyHistory(models.Model):
    _name = 'hospital.patient.colposcopy.history'
    _description = 'Hospital Patient Colposcopy History'

    patient_id = fields.Many2one('hospital.patient', 'Patient')
    ovulation_id = fields.Many2one('hospital.patient.ovulation', 'Ovulation')
    result = fields.Selection([('negative', 'Negative'),
                               ('c1', 'ASC-US'),
                               ('c2', 'ASC-H'),
                               ('g1', 'ASG'),
                               ('c3', 'LSIL'),
                               ('c4', 'HISL'),
                               ('g4', 'AIS')], 'Result')
    remark = fields.Char('Remark')
    ovulation_date = fields.Datetime('Ovulation Date')
