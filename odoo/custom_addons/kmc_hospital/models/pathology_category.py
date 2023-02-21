from odoo import models, fields, api, _


class HospitalPathologyCategory(models.Model):
    _name = 'hospital.pathology.category'
    _description = 'Hospital Pathology Category'

    name = fields.Char(string="Category Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    parent_id = fields.Many2one('hospital.pathology.category', string="Parent Category")
