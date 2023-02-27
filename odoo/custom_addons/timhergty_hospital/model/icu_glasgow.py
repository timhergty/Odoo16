from odoo import models, fields, api, _
from datetime import date, datetime


class HospitalIcuGlasgow(models.Model):
    _name = 'hospital.icu.glasgow'
    _description = 'Hospital Icu Glasgow'
    _rec_name = 'hospital_inpatient_registration_id'

    hospital_inpatient_registration_id = fields.Many2one('hospital.inpatient.registration', string="Registration Code",
                                                         required=True)
    evaluation_date = fields.Datetime(string="Date", required=True)
    glasgow_eyes = fields.Selection([('1', '1 : Does not Open Eyes'),
                                     ('2', '2 : Opens eyes in response to painful Stimuli'),
                                     ('3', '3 : Open eyes to response to voice'),
                                     ('4', '4 : Open eyes spontaneously')],
                                    string="Eyes")
    glasgow_verbal = fields.Selection([('1', '1 : Makes no sounds'),
                                       ('2', '2 : Incomprehensible Sounds'),
                                       ('3', '3 : Utters Inappropriate words'),
                                       ('4', '4 : Confused disoriented'),
                                       ('5', '5 : Oriented converses normally')],
                                      string="Verbal")
    glasgow_motor = fields.Selection([('1', '1 : Makes no movement'),
                                      ('2', '2 : Extension to painful stimuli -decerabrate response'),
                                      ('3', '3 : Abnormal flexion to painful stimuli (decorticate response)'),
                                      ('4', '4 : Flexion/Withdrawal to painful stimuli'),
                                      ('5', '5 : Localizes painful stimuli'),
                                      ('6', '6 : Obeys commands')],
                                     string="Motor")
    glasgow = fields.Integer(string="Glasgow", compute='get_glas_score')

    @api.depends('glasgow_motor', 'glasgow_verbal', 'glasgow_eyes')
    def get_glas_score(self):
        """ Calculates Sub total"""
        count = int(self.glasgow_eyes) + int(self.glasgow_motor) + int(self.glasgow_verbal)
        self.glasgow = count
