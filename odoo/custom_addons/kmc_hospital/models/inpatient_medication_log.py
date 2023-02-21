from odoo import models, fields, api, _
from datetime import date, datetime


class HospitalInpatientMedicationLog(models.Model):
    _name = 'hospital.inpatient.medication.log'
    _description = 'Hospital Inpatient medication Log'

    admin_time = fields.Datetime(string='Date', readonly=True)
    dose = fields.Float(string='Dose')
    remarks = fields.Text(string='Remarks')
    hospital_inpatient_medication_log_id = fields.Many2one('hospital.physician', string='Health Professional',
                                                           readonly=True)
    hospital_dose_unit_id = fields.Many2one('hospital.dose.unit', string='Dose Unt')
    hospital_inpatient_log_medicament_id = fields.Many2one('hospital.inpatient.medication', string='Log History')
