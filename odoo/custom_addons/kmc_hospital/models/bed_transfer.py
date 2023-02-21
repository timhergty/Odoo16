from odoo import models, fields, api, _
from datetime import date


class BedTransfer(models.Model):
    _name = 'bed.transfer'
    _description = "Bed Transfer"

    name = fields.Char("Name")
    date = fields.Datetime(string='Date')
    bed_from = fields.Char(string='From')
    bed_to = fields.Char(string='To')
    reason = fields.Text(string='Reason')
    inpatient_id = fields.Many2one('hospital.inpatient.registration', string='Inpatient Id')
