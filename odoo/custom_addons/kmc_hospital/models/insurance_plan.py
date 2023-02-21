from odoo import api, fields, models, _


class HospitalInsurancePlan(models.Model):
    _name = 'hospital.insurance.plan'
    _description = 'Hospital Insurance Plan'
    _rec_name = 'insurance_product_id'

    insurance_product_id = fields.Many2one('product.product', 'Plan', domain="[('type','=','service')]")
    is_default = fields.Boolean('Default Plan')
    company_partner_id = fields.Many2one('res.partner', domain=[('is_insurance_company', '=', True)], string='Company')
    notes = fields.Text('Extra Info')
