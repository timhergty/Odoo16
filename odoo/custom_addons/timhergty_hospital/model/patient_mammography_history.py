from odoo import api, fields, models, _
from datetime import date, datetime


class HospitalPatientMammographyHistory(models.Model):
    _name = 'hospital.patient.mammography.history'
    _description = 'Hospital Patient Mammography History'

    patient_id = fields.Many2one('hospital.patient', 'Patient')
    ovulation_id = fields.Many2one('hospital.patient.ovulation', 'Ovulation')
    evolution_date = fields.Date('Date')
    last_mamography_date = fields.Date('Date')
    result = fields.Selection([('normal', 'Normal'), ('abnormal', 'Abnormal')])
    remark = fields.Char('Comments')
