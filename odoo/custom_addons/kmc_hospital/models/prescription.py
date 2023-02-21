from odoo import api, fields, models, _
from datetime import date, datetime


class PrescriptionLine(models.Model):
    _name = "hospital.prescription.line"
    _description = 'Hospital Prescription Line'

    name = fields.Many2one('hospital.prescription.order', 'Prescription ID')
    medicament_id = fields.Many2one('hospital.medicament', 'Medicament')
    indication = fields.Char('Indication')
    allow_substitution = fields.Boolean('Allow Substitution')
    form = fields.Char('Form')
    prnt = fields.Boolean('Print')
    route = fields.Char('Administration Route')
    end_treatment = fields.Datetime('Administration Route')
    dose = fields.Float('Dose')
    dose_unit_id = fields.Many2one('hospital.dose.unit', 'Dose Unit')
    qty = fields.Integer('x')
    medication_dosage_id = fields.Many2one('hospital.medication.dosage', 'Frequency')
    admin_times = fields.Char('Admin Hours', size=128)
    frequency = fields.Integer('Frequency')
    frequency_unit = fields.Selection(
        [('seconds', 'Seconds'), ('minutes', 'Minutes'), ('hours', 'hours'), ('days', 'Days'), ('weeks', 'Weeks'),
         ('wr', 'When Required')], 'Unit')
    duration = fields.Integer('Treatment Duration')
    duration_period = fields.Selection(
        [('minutes', 'Minutes'), ('hours', 'hours'), ('days', 'Days'), ('months', 'Months'), ('years', 'Years'),
         ('indefine', 'Indefine')], 'Treatment Period')
    quantity = fields.Integer('Quantity')
    review = fields.Datetime('Review')
    refills = fields.Integer('Refills#')
    short_comment = fields.Char('Comment', size=128)
    end_treatment = fields.Datetime('End of treatment')
    start_treatment = fields.Datetime('Start of treatment')
