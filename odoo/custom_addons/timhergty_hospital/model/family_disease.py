from odoo import api, fields, models, _


class HospitalFamilyDisease(models.Model):
    _name = 'hospital.family.disease'
    _description = 'Hospital Family Disease'
    _rec_name = 'hospital_pathology_id'

    hospital_pathology_id = fields.Many2one('hospital.pathology', 'Disease', required=True)
    relative = fields.Selection(
        [('m', 'Mother'), ('f', 'Father'), ('b', 'Brother'), ('s', 'Sister'), ('a', 'aunt'), ('u', 'Uncle'),
         ('ne', 'Nephew'), ('ni', 'Niece'), ('gf', 'GrandFather'), ('gm', 'GrandMother')], string="Relative")
    maternal = fields.Selection([('m', 'Maternal'), ('p', 'Paternal')], string="Maternal")
