from odoo import models, fields, api, _
from datetime import date, datetime


class HospitalInpatientMedicationAdminTime(models.Model):
    _name = 'hospital.inpatient.medication.admin.time'
    _description = 'Hospital Inpatient Medication Admin Time'

    admin_time = fields.Datetime(string='Date')
    dose = fields.Float(string='Dose')
    remarks = fields.Text(string='Remarks')
    hospital_inpatient_admin_time_id = fields.Many2one('hospital.physician', string='Health Professional')
    dose_unit = fields.Many2one('hospital.dose.unit', string='Dose Unt')
    hospital_inpatient_admin_time_medicament_id = fields.Many2one('hospital.inpatient.medication', string='Admin Time')
