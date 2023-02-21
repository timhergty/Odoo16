from odoo import models, fields, api, _


class HospitalDietBelief(models.Model):
    _name = 'hospital.diet.belief'
    _description = 'Hospital Diet Belief'

    code = fields.Char(string='Code', required=True)
    description = fields.Text(string='Description', required=True)
    name = fields.Char(string='Belief')

