from odoo import models, fields, api, _


class HospitalPathologyGroup(models.Model):
    _name = 'hospital.pathology.group'
    _description = 'Hospital Pathology Group'

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code")
    desc = fields.Char(string="Short Description", required=True)
    info = fields.Text(string="Detailed Information")
