from odoo import api, fields, models, _


class HospitalLabTestUnits(models.Model):
    _name = 'hospital.lab.test.units'
    _description = 'Hospital Lab Test Units'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code')
