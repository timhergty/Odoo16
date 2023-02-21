from odoo import models, fields, api, _


class HospitalInpatientDiet(models.Model):
    _name = 'hospital.inpatient.diet'
    _description = 'Hospital Inpatient Diet'

    diet_id = fields.Many2one('hospital.diet.therapeutic', string='Diet', required=True)
    remarks = fields.Text(string=' Remarks / Directions ')
    hospital_inpatient_registration_id = fields.Many2one('hospital.inpatient.registration', string='Inpatient Id')

