from odoo import models, fields, api, _
from datetime import date, datetime


class HospitalInpatientRegistration(models.Model):
    _name = 'hospital.inpatient.registration'
    _description = 'Hospital Inpatient Registration'

    name = fields.Char(string="Registration Code", copy=False, readonly=True, index=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    hospitalization_date = fields.Datetime(string="Hospitalization date", required=True)
    discharge_date = fields.Datetime(string="Expected Discharge date", required=True)
    attending_physician_id = fields.Many2one('hospital.physician', string="Attending Physician")
    operating_physician_id = fields.Many2one('hospital.physician', string="Operating Physician")
    admission_type = fields.Selection(
        [('routine', 'Routine'), ('maternity', 'Maternity'), ('elective', 'Elective'), ('urgent', 'Urgent'),
         ('emergency', 'Emergency  ')], required=True, string="Admission Type")
    hospital_pathology_id = fields.Many2one('hospital.pathology', string="Reason for Admission")
    info = fields.Text(string="Extra Info")
    bed_transfers_ids = fields.One2many('bed.transfer', 'inpatient_id', string='Transfer Bed')
    hospital_diet_belief_id = fields.Many2one('hospital.diet.belief', string='Belief')
    therapeutic_diets_ids = fields.One2many('hospital.inpatient.diet', 'hospital_inpatient_registration_id',
                                            string='Therapeutic_diets')
    diet_vegetarian = fields.Selection([('none', 'None'), ('vegetarian', 'Vegetarian'), ('lacto', 'Lacto Vegetarian'),
                                        ('lactoovo', 'Lacto-Ovo-Vegetarian'), ('pescetarian', 'Pescetarian'),
                                        ('vegan', 'Vegan')], string="Vegetarian")
    nutrition_notes = fields.Text(string="Nutrition notes / Directions")
    state = fields.Selection(
        [('free', 'Free'), ('confirmed', 'Confirmed'), ('hospitalized', 'Hospitalized'), ('cancel', 'Cancel'),
         ('done', 'Done')], string="State", default="free")
    nursing_plan = fields.Text(string="Nursing Plan")
    discharge_plan = fields.Text(string="Discharge Plan")
    icu = fields.Boolean(string="ICU")
    medication_ids = fields.One2many('hospital.inpatient.medication', 'hospital_inpatient_registration_id',
                                     string='Medication')

    @api.model
    def default_get(self, fields):
        result = super(HospitalInpatientRegistration, self).default_get(fields)
        patient_id = self.env['ir.sequence'].next_by_code('hospital.inpatient.registration')
        if patient_id:
            result.update({
                'name': patient_id,
            })
        return result

    def registration_confirm(self):
        self.write({'state': 'confirmed'})

    def registration_admission(self):
        self.write({'state': 'hospitalized'})

    def registration_cancel(self):
        self.write({'state': 'cancel'})

    def patient_discharge(self):
        self.write({'state': 'done'})
