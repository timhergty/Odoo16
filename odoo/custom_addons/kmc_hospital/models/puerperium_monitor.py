from odoo import api, fields, models, _
from datetime import date, datetime


class HospitalPuerperiumMonitor(models.Model):
    _name = 'hospital.puerperium.monitor'
    _description = 'Hospital Puerperium Monitor'

    pregnancy_id = fields.Many2one('hospital.patient.pregnancy')
    date = fields.Datetime('Date And Time')
    systolic_pressure = fields.Integer('Systolic Pressure')
    diastolic_pressure = fields.Integer('Diastolic Pressure')
    heart_freq = fields.Integer('Heart Frequency')
    temprature = fields.Integer('Temperature')
    fundal_height = fields.Integer('Fundal Height')
    lochia_amount = fields.Selection([('n', 'Normal'), ('a', 'Abudant'), ('h', 'Hemorrhage'), ], 'Lochia amount')
    lochia_color = fields.Selection([('r', 'Rubra'), ('s', 'Serosa'), ('a', 'Alba')], 'Loicha Color')
    loicha_order = fields.Selection([('n', 'Normal'), ('o', 'Offensive')], 'Loicha Order')
