from odoo import api, fields, models, _
from datetime import date, datetime


class HospitalPatientPregnancy(models.Model):
    _name = 'hospital.patient.pregnancy'
    _description = 'Hospital Patient Pregnancy'

    gravida = fields.Integer('Pregnancy #')
    lmp = fields.Integer('LMP')
    pdd = fields.Date('Pregnancy  Due Date')
    patient_id = fields.Many2one('hospital.patient', 'Patient')
    current_pregnancy = fields.Boolean('Current Pregnancy')
    hospital_patient_evaluation_prenatal_ids = fields.One2many('hospital.patient.prenatal.evaluation', 'pregnancy_id',
                                                               'Patient Perinatal Evaluations')
    hospital_prenatal_ids = fields.One2many('hospital.prenatal', 'pregnancy_id', 'hospital Prenatal')
    puerperium_perental_ids = fields.One2many('hospital.puerperium.monitor', 'pregnancy_id', 'Puerperium Monitor')
    fetuses = fields.Boolean('Fetuses')
    monozygotic = fields.Boolean('Monozygotic')
    igur = fields.Selection([('s', 'Symmetric'), ('a', 'Asymmetric')], 'IGUR')
    warn = fields.Boolean('Warning')
    result = fields.Char('Result')
    pregnancy_end_date = fields.Date('Pregnancy End Date')
    pregnancy_end_result = fields.Char('Pregnancy End Result')
