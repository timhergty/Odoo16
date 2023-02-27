from odoo import api, fields, models, _
from datetime import date, datetime


class HospitalPerinatalMonitor(models.Model):
    _name = 'hospital.perinatal.monitor'
    _description = 'Hospital Perinatal Monitor'

    hospital_perinatal_id = fields.Many2one('hospital.perinatal.monitor')
    date = fields.Date('Date')
    systolic = fields.Integer('Systolic Pressure')
    diastolic = fields.Integer('Diastolic Pressure')
    mothers_heart_freq = fields.Integer('Mothers Heart Freq')
    concentration = fields.Integer('Concentration')
    cervix_dilation = fields.Integer('Cervix Dilation')
    fundel_height = fields.Integer('Fundel Height')
    fetus_presentation = fields.Selection([('n', 'Correct'),
                                           ('o', 'Occiput /Cephalic Postrior'),
                                           ('fb', 'Frank Breech'),
                                           ('cb', 'Complete Breech'),
                                           ('tl', 'Transverse Lie'),
                                           ('fu', 'Footling Lie')], 'Fetus Presentation')
    f_freq = fields.Integer('Fetus Heart Frequency')
    bleeding = fields.Boolean('Bleeding')
    meconium = fields.Boolean('Meconium')
    notes = fields.Char('Notes')