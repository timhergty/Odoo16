from odoo import api, fields, models, _
from datetime import date, datetime
from odoo.exceptions import UserError, ValidationError


class HospitalPatientLabTest(models.Model):
    _name = 'hospital.patient.lab.test'
    _description = 'hospital patient lab test'
    _rec_name = 'hospital_test_type_id'

    request = fields.Char('Request', readonly=True)
    date = fields.Datetime('Date', default=fields.Datetime.now)
    lab_test_owner_partner_id = fields.Many2one('res.partner', 'Owner Name')
    urgent = fields.Boolean('Urgent', )
    owner_partner_id = fields.Many2one('res.partner')
    state = fields.Selection([('draft', 'Draft'), ('tested', 'Tested'), ('cancel', 'Cancel')], readonly=True,
                             default='draft')
    hospital_test_type_id = fields.Many2one('hospital.test_type', 'Test Type', required=True)
    patient_id = fields.Many2one('hospital.patient', 'Patient')
    doctor_id = fields.Many2one('hospital.physician', 'Doctor', required=True)
    insurer_id = fields.Many2one('hospital.insurance', 'Insurer')
    invoice_to_insurer = fields.Boolean('Invoice to Insurance')
    lab_res_created = fields.Boolean(default=False)
    is_invoiced = fields.Boolean(copy=False, default=False)

    @api.model
    def create(self, vals):
        vals['request'] = self.env['ir.sequence'].next_by_code('test_seq')
        result = super(HospitalPatientLabTest, self).create(vals)
        return result

    def cancel_lab_test(self):
        self.write({'state': 'cancel'})

    def create_lab_test(self):
        res_ids = []
        for browse_record in self:
            result = {}
            hospital_lab_obj = self.env['hospital.lab']
            res = hospital_lab_obj.create({
                'name': self.env['ir.sequence'].next_by_code('ltest_seq'),
                'patient_id': browse_record.patient_id.id,
                'date_requested': browse_record.date or False,
                'test_id': browse_record.hospital_test_type_id.id or False,
                'requestor_physician_id': browse_record.doctor_id.id or False,
            })
            res_ids.append(res.id)
            if res_ids:
                imd = self.env['ir.model.data']
                action = self.env.ref('kmc_hospital.action_hospital_lab_form')
                list_view_id = imd.sudo()._xmlid_to_res_id('kmc_hospital.hospital_lab_tree_view')
                form_view_id = imd.sudo()._xmlid_to_res_id('kmc_hospital.hospital_lab_form_view')
                result = {
                    'name': action.name,
                    'help': action.help,
                    'type': action.type,
                    'views': [[list_view_id, 'tree'], [form_view_id, 'form']],
                    'target': action.target,
                    'context': action.context,
                    'res_model': action.res_model,
                    'res_id': res.id,

                }

            if res_ids:
                result['domain'] = "[('id','=',%s)]" % res_ids

        return result
