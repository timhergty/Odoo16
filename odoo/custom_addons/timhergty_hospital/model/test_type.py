from odoo import api, fields, models, _


# classes under configuration menu of laboratory

class HospitalTestType(models.Model):
    _name = 'hospital.test_type'
    _description = 'Hospital Test Type'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    seq = fields.Integer('Sequence', default=1)
    criteria_ids = fields.One2many('hospital_test.criteria', 'test_id', 'Criteria')
    service_product_id = fields.Many2one('product.product', 'Service', required=True)
    info = fields.Text('Extra Information')
