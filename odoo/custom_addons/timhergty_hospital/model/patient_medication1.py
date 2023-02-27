from odoo import api, fields, models, _
from datetime import date, datetime


class HospitalPatientMedication1(models.Model):
    _name = 'hospital.patient.medication1'
    _description = 'Hospital Patient Medication1'
    _rec_name = 'hospital_patient_medication_id'

    hospital_medicament_id = fields.Many2one('hospital.medicament', string='Medicament', required=True)
    hospital_patient_medication_id = fields.Many2one('hospital.patient', string='Medication')
    is_active = fields.Boolean(string='Active', default=True)
    start_treatment = fields.Datetime(string='Start Of Treatment', required=True)
    course_completed = fields.Boolean(string="Course Completed")
    doctor_physician_id = fields.Many2one('hospital.physician', string='Physician')
    indication_pathology_id = fields.Many2one('hospital.pathology', string='Indication')
    end_treatment = fields.Datetime(string='End Of Treatment', required=True)
    discontinued = fields.Boolean(string='Discontinued')
    drug_route_id = fields.Many2one('hospital.drug.route', string=" Administration Route ")
    dose = fields.Float(string='Dose')
    qty = fields.Integer(string='X')
    dose_unit_id = fields.Many2one('hospital.dose.unit', string='Dose Unit')
    duration = fields.Integer(string="Treatment Duration")
    duration_period = fields.Selection([('minutes', 'Minutes'),
                                        ('hours', 'hours'),
                                        ('days', 'Days'),
                                        ('months', 'Months'),
                                        ('years', 'Years'),
                                        ('indefine', 'Indefine')], string='Treatment Period')
    medication_dosage_id = fields.Many2one('hospital.medication.dosage', string='Frequency')
    admin_times = fields.Char(string='Admin Hours')
    frequency = fields.Integer(string='Frequency')
    frequency_unit = fields.Selection([('seconds', 'Seconds'),
                                       ('minutes', 'Minutes'),
                                       ('hours', 'hours'),
                                       ('days', 'Days'),
                                       ('weeks', 'Weeks'),
                                       ('wr', 'When Required')], string='Unit')
    notes = fields.Text(string='Notes')