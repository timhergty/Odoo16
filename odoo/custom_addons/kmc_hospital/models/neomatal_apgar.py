from odoo import api, fields, models, _
from datetime import date, datetime


class HospitalNeomatalApgar(models.Model):
    _name = 'hospital.neomatal.apgar'
    _description = 'Hospital Neomatal Apgar'
    _rec_name = 'apgar_appearance'

    apgar_activity = fields.Selection([('0', 'None'), ('1', 'Some Flexion'), ('2', 'Fixed Arm and Legs')], 'Activity')
    apgar_appearance = fields.Selection([('0', 'Central cyanosis'), ('1', 'Acrosynosis'), ('2', 'No Cynosis')],
                                        'Appearance')
    apgar_grimace = fields.Selection([('0', 'No response to simulation'), ('1', 'Grimance when simulated'),
                                      ('2', 'Cry Or pull away when simulated')], 'Grimace')
    apgar_minute = fields.Integer('Minute', required=True)
    apgar_respiration = fields.Selection([('0', 'Absent'), ('1', 'Weak / Irregular'), ('2', 'Strong')], 'Respiration')
    apgar_pulse = fields.Selection([('0', 'None'), ('1', '< 100'), ('2', '> 100')], 'Pulse')
    apgar_scores = fields.Integer('Apgar Score')

    @api.onchange('apgar_activity', 'apgar_appearance', 'apgar_grimace', 'apgar_minute', 'apgar_respiration',
                  'apgar_pulse', )
    def on_change_selection(self):
        self.apgar_scores = int(self.apgar_activity) + int(self.apgar_appearance) + int(self.apgar_grimace) + int(
            self.apgar_minute) + int(self.apgar_respiration) + int(self.apgar_pulse)
