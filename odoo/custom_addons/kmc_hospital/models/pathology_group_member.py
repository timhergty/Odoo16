from odoo import models, fields, api, _


class HospitalPathologyGroupMember(models.Model):
    _name = 'hospital.pathology.group.member'
    _description = 'Hospital Pathology Group Member'

    disease_group_id = fields.Many2one('hospital.pathology.group', string="Group", required=True)
