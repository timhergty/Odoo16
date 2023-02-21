from odoo import api, fields, models, _


class HospitalTestCriteria(models.Model):
    _name = 'hospital_test.criteria'
    _description = 'Hospital Test Criteria'

    test_id = fields.Many2one('hospital.test_type', )
    name = fields.Char('Name', )
    seq = fields.Integer('Sequence')
    hospital_test_type_id = fields.Many2one('hospital.test_type', 'Test Type')
    hospital_lab_id = fields.Many2one('hospital.lab', 'hospital Lab Result')
    warning = fields.Boolean('Warning')
    excluded = fields.Boolean('Excluded')
    lower_limit = fields.Float('Lower Limit')
    upper_limit = fields.Float('Upper Limit')
    lab_test_unit_id = fields.Many2one('hospital.lab.test.units', 'Units')
    result = fields.Float('Result')
    result_text = fields.Char('Result Text')
    normal_range = fields.Char('Normal Range')
    remark = fields.Text('Remarks')