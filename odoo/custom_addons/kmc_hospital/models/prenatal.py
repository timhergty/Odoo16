from odoo import api, fields, models, _
from datetime import date, datetime


class HospitalPrenatal(models.Model):
    _name = 'hospital.prenatal'
    _description = 'Hospital Prenatal'

    pregnancy_id = fields.Many2one('hospital.patient.pregnancy', 'Pregnancy', )
    gestational_weeks = fields.Integer('Gestational weeks')
    admission_date = fields.Date('Admission Date')
    code = fields.Char('Code')
    labour_mode = fields.Selection([('n', 'Normal'), ('i', 'Induced'), ('c', 'C-Section')], 'Labour Mode')
    fetus_presentation = fields.Selection([('n', 'Correct'),
                                           ('o', 'Occiput /Cephalic Posterior'),
                                           ('fb', 'Frank Breech'),
                                           ('cb', 'Complete Breech'),
                                           ('tl', 'Transverse Lie'),
                                           ('fu', 'Footling Lie')], 'Fetus Presentation')
    monitor_ids = fields.One2many('hospital.prenatal.monitor', 'hospital_prenatal_id')
    dystopia = fields.Boolean('Dystopia')
    episiotomy = fields.Boolean('Epitomises')
    lacerations = fields.Selection([('p', 'Perinial'),
                                    ('v', 'Vaginal'),
                                    ('c', 'Cervical'),
                                    ('bl', 'Broad Ligament'),
                                    ('vl', 'Vulvar'),
                                    ('r', 'Rectal'),
                                    ('br', 'Blader'),
                                    ('u', 'Ureteral'), ], 'Lacerations')

    hematoma = fields.Selection([('v', 'Vaginal'), ('vl', 'Vulvar'), ('r', 'Retroperitional')], 'Hematoma')
    plancenta_incomplete = fields.Boolean('Incomplete Placenta')
    retained_placenta = fields.Boolean('Retained Placenta')
    abruptio_placentae = fields.Boolean('Abruptio Placentae')

    notes = fields.Text('Notes')
