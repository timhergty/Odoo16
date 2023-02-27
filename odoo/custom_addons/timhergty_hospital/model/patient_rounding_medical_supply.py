from odoo import api, fields, models, _


class HospitalPatientRoundingMedicalSupply(models.Model):
    _name = 'hospital.patient.rounding.medical_supply'
    _description = 'Hospital Patient Rounding Medical Supply'

    product_id = fields.Many2one('product.product', string="Medical Supply", required=True)
    short_comment = fields.Char(string='Comment')
    quantity = fields.Integer(string="Quantity")
    lot_id = fields.Many2one('stock.production.lot', string='Lot', required=True)
    hospital_patient_rounding_medical_supply_id = fields.Many2one('hospital.patient.rounding',
                                                                   string=" Medical Supplies ")
