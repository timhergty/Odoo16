from odoo import api, fields, models, _
from datetime import date, datetime


class HospitalPatientCage(models.Model):
    _name = 'hospital.patient.cage'
    _description = 'hospital patient cage'
    _rec_name = 'patient_id'

    @api.onchange('cage_c', 'cage_a', 'cage_g', 'cage_e')
    def get_score(self):
        self.cage_score = int(self.cage_c) + int(self.cage_a) + int(self.cage_g) + int(self.cage_e)

    patient_id = fields.Many2one('hospital.patient')
    ovulation_date = fields.Datetime()
    cage_c = fields.Boolean(default=False)
    cage_a = fields.Boolean(default=False)
    cage_g = fields.Boolean(default=False)
    cage_e = fields.Boolean(default=False)
    cage_score = fields.Integer('Cage Score', default=0)