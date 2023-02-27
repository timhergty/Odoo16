from odoo import api, fields, models, _
from datetime import date, datetime


class HospitalPatientPerinatalOvulation(models.Model):
    _name = 'hospital.patient.perinatal.ovulation'
    _description = 'hospital Patient Perinatal ovulation'

    pregnancy_id = fields.Many2one('hospital.patient.pregnancy', )
    ovulation_date = fields.Date('Date', required=True)
    gestational_weeks = fields.Integer('Gestational Weeks', required=True)
    hypertansion = fields.Boolean('Hypertension')
    preclampsia = fields.Boolean('Prclampsia')
    overweight = fields.Boolean('Overweight')
    diabetes = fields.Boolean('Diabetes')
    placenta_previa = fields.Boolean('Placenta Previa')
    invasive_placentation = fields.Selection([('normal_decidua', 'Normal Decidua'),
                                              ('accreta', 'Accreta'),
                                              ('increta', 'Increta'),
                                              ('percreta', 'Precreta')])
    vasa_previa = fields.Boolean('Vasa Previa')
    fundel_weight = fields.Integer('Fundel Weight')
    fetus_heart_rate = fields.Integer('Fetus Heart Rate')
    efw = fields.Integer('EFW')
    bpd = fields.Integer('BPD')
    hc = fields.Integer('HC')
    ac = fields.Integer('AC')
    fl = fields.Integer('FL')
