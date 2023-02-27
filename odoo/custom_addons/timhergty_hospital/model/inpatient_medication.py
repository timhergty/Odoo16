from odoo import models, fields, api, _
from datetime import date, datetime


class HospitalInpatientMedication(models.Model):
    _name = 'hospital.inpatient.medication'
    _description = 'Hospital Inpatient Medication'
    _rec_name = 'hospital_medicament_id'

    hospital_medicament_id = fields.Many2one('hospital.medicament', string='Medicament', required=True)
    is_active = fields.Boolean(string='Active')
    start_treatment = fields.Datetime(string='Start Of Treatment', required=True)
    course_completed = fields.Boolean(string="Course Completed")
    hospital_inpatient_medication_physician_id = fields.Many2one('hospital.physician', string='Physician')
    hospital_pathology_id = fields.Many2one('hospital.pathology', string='Indication')
    end_treatment = fields.Datetime(string='End Of Treatment', required=True)
    discontinued = fields.Boolean(string='Discontinued')
    hospital_drug_route_id = fields.Many2one('hospital.drug.route', string=" Administration Route ")
    dose = fields.Float(string='Dose')
    qty = fields.Integer(string='X')
    hospital_dose_unit_id = fields.Many2one('hospital.dose.unit', string='Dose Unit')
    duration = fields.Integer(string="Treatment Duration")
    duration_period = fields.Selection([('minutes', 'Minutes'),
                                        ('hours', 'hours'),
                                        ('days', 'Days'),
                                        ('months', 'Months'),
                                        ('years', 'Years'),
                                        ('indefine', 'Indefinite')], string='Treatment Period')
    hospital_medication_dosage_id = fields.Many2one('hospital.medication.dosage', string='Frequency')
    admin_times = fields.Char(string='Admin Hours')
    frequency = fields.Integer(string='Frequency')
    frequency_unit = fields.Selection([('seconds', 'Seconds'),
                                       ('minutes', 'Minutes'),
                                       ('hours', 'hours'),
                                       ('days', 'Days'),
                                       ('weeks', 'Weeks'),
                                       ('wr', 'When Required')], string='Unit')
    adverse_reaction = fields.Text(string='Notes')
    hospital_inpatient_registration_id = fields.Many2one('hospital.inpatient.registration', string='Medication')
    inpatient_admin_times_ids = fields.One2many('hospital.inpatient.medication.admin.time',
                                                'hospital_inpatient_admin_time_medicament_id', string='Admin')
    inpatient_log_history_ids = fields.One2many('hospital.inpatient.medication.log',
                                                'hospital_inpatient_log_medicament_id', string='Log History')
