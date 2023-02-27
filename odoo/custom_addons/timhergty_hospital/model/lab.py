from odoo import api, fields, models, _
from datetime import date, datetime


class HospitalLab(models.Model):
    _name = 'hospital.lab'
    _description = 'hospital Lab'

    name = fields.Char('ID')
    test_id = fields.Many2one('hospital.test_type', 'Test Type', required=True)
    date_analysis = fields.Datetime('Date of the Analysis', default=datetime.now())
    patient_id = fields.Many2one('hospital.patient', 'Patient', required=True)
    date_requested = fields.Datetime('Date requested', default=datetime.now())
    hospital_lab_physician_id = fields.Many2one('hospital.physician', 'Pathologist')
    requestor_physician_id = fields.Many2one('hospital.physician', 'Physician', required=True)
    criteria_ids = fields.One2many('hospital_test.criteria', 'hospital_lab_id', 'Criteria')
    results = fields.Text('Results')
    diagnosis = fields.Text('Diagnosis')
    is_invoiced = fields.Boolean(copy=False, default=False)

    @api.model_create_multi
    def create(self, vals_list):
        vals_list['name'] = self.env['ir.sequence'].next_by_code('ltest_seq')
        result = super(HospitalLab, self).create(vals_list)
        if vals_list.get('test_id'):
            criteria_obj = self.env['hospital_test.criteria']
            criteria_ids = criteria_obj.search([('test_id', '=', vals_list['test_id'])])
            for id in criteria_ids:
                criteria_obj.write({'hospital_lab_id': result})

        return result
