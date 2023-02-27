from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    relationship = fields.Char(string='Relationship')
    relative_partner_id = fields.Many2one('res.partner', string="Relative_id")
    is_patient = fields.Boolean(string='Patient')
    is_person = fields.Boolean(string="Person")
    is_doctor = fields.Boolean(string="Doctor")
    is_insurance_company = fields.Boolean(string='Insurance Company')
    is_pharmacy = fields.Boolean(string="Pharmacy")
    patient_insurance_ids = fields.One2many('hospital.insurance', 'patient_id')
    is_institution = fields.Boolean('Institution')
    company_insurance_ids = fields.One2many('hospital.insurance', 'insurance_company_id', 'Insurance')
    reference = fields.Char('ID Number')
