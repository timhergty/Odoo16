from odoo import api, fields, models, _


class HospitalPatientRoundingMedicament(models.Model):
    _name = 'hospital.patient.rounding.medicament'
    _description = 'Hospital patient rounding medicament'

    medicament_id = fields.Many2one('hospital.medicament', string='Medicament', required=True)
    quantity = fields.Integer(string="Quantity")
    lot_id = fields.Many2one('stock.production.lot', string='Lot', required=True)
    short_comment = fields.Char(string='Comment')
    product_id = fields.Many2one('product.product', string='Product')
    hospital_patient_rounding_medicament_id = fields.Many2one('hospital.patient.rounding', string="Medicaments")
