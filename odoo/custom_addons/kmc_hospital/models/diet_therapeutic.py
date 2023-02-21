from odoo import models, fields, api, _


class HospitalDietTherapeutic(models.Model):
    _name = 'hospital.diet.therapeutic'
    _description = 'Hospital Diet Therapeutic'

    name = fields.Char(string='Diet Type', required=True)
    code = fields.Char(string='Code', required=True)
    description = fields.Text(string='Description', required=True)

