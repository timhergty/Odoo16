from odoo import api, fields, models, _


class HospitalDrugRoute(models.Model):
    _name = 'hospital.drug.route'
    _description = 'Hospital Drug Route'

    name = fields.Char(string="Route", required=True)
    code = fields.Char(string="Code")
