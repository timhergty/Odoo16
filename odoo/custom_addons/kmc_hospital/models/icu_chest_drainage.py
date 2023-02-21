from odoo import api, fields, models, _


class HospitalIcuChestDrainage(models.Model):
    _name = 'hospital.icu.chest_drainage'
    _description = 'Hospital Icu Chest Drainage'

    location = fields.Selection([('rl', 'Right Pleura'),
                                 ('ll', 'Left Pleura'),
                                 ('mediastinum', 'Mediastinum')],
                                string='Location')
    suction = fields.Boolean(string="Suction")
    suction_pressure = fields.Integer(string="cm H2O")
    fluid_volume = fields.Integer(string="Volume")
    fluid_aspect = fields.Selection([('serous', 'Serous'),
                                     ('bloody', 'Bloody'),
                                     ('chylous', 'Chylous'),
                                     ('purulent', 'Purulent')],
                                    string="Aspect")
    oscillation = fields.Boolean(string='Oscillation')
    air_leak = fields.Boolean(string='Air Leak')
    remarks = fields.Char(string="Remarks")
    hospital_patient_rounding_chest_drainage_id = fields.Many2one('hospital.patient.rounding', string="Chest Drainage")
