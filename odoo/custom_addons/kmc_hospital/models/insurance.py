from odoo import models, fields, api, _


class HospitalInsurance(models.Model):
    _name = 'hospital.insurance'
    _description = 'Hospital Insurance'
    _rec_name = 'insurance_company_id'

    number = fields.Char('Number')
    hospital_insurance_partner_id = fields.Many2one('res.partner', 'Owner', required=True)
    patient_id = fields.Many2one('res.partner', 'Owner')
    type = fields.Selection([('state', 'State'), ('private', 'Private'), ('labour_union', 'Labour Union/ Syndical')],
                            'Insurance Type')
    member_since = fields.Date('Member Since')
    insurance_company_id = fields.Many2one('res.partner', domain=[('is_insurance_company', '=', True)],
                                           string='Insurance Company')
    category = fields.Char('Category')
    notes = fields.Text('Extra Info')
    member_exp = fields.Date('Expiration Date')
    hospital_insurance_plan_id = fields.Many2one('hospital.insurance.plan', 'Plan')
