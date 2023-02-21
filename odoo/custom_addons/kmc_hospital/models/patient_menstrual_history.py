from odoo import api, fields, models, _
from datetime import date, datetime


class HospitalPatientMenstrualHistory(models.Model):
    _name = 'hospital.patient.menstrual.history'
    _description = 'Hospital Patient Menstrual History'

    patient_id = fields.Many2one('hospital.patient', 'Patient')
    evolution_id = fields.Many2one('hospital.patient.evaluation', 'Evaluation')
    evoultion_date = fields.Date('Date')
    lmp = fields.Integer('LMP', required=True)
    lmp_length = fields.Integer('LMP Length', required=True)
    is_regular = fields.Boolean('IS Regular')
    dysmenorrhea = fields.Boolean('Dysmenorrhea')
    frequency = fields.Selection([('amenorrhea', 'Amenorrhea'),
                                  ('oligomenorrhea', 'Oligomenorrhea'),
                                  ('eumenorrhea', 'Eumenorrhea'),
                                  ('pollymenohea', 'Pollymenohea')])
    volume = fields.Selection([('hopomenorrhea', 'hopomenorrhea'),
                               ('normal', 'Normal'),
                               ('menorrhagia', 'Menorrhagia')])
