from odoo import api, fields, models, _
from datetime import date, datetime


class HospitalPrescriptionOrder(models.Model):
    _name = "hospital.prescription.order"
    _description = 'Hospital Prescription Order'

    name = fields.Char('Prescription ID')
    patient_id = fields.Many2one('hospital.patient', 'Patient ID')
    prescription_date = fields.Datetime('Prescription Date', default=fields.Datetime.now)
    user_id = fields.Many2one('res.users', 'Login User', readonly=True, default=lambda self: self.env.user)
    no_invoice = fields.Boolean('Invoice exempt')
    inv_id = fields.Many2one('account.invoice', 'Invoice')
    invoice_to_insurer = fields.Boolean('Invoice to Insurance')
    doctor_id = fields.Many2one('hospital.physician', 'Prescribing Doctor')
    hospital_appointment_id = fields.Many2one('hospital.appointment', 'Appointment')
    state = fields.Selection([('invoiced', 'To Invoiced'), ('tobe', 'To Be Invoiced')], 'Invoice Status')
    pharmacy_partner_id = fields.Many2one('res.partner', domain=[('is_pharmacy', '=', True)], string='Pharmacy')
    prescription_line_ids = fields.One2many('hospital.prescription.line', 'name', 'Prescription Line')
    invoice_done = fields.Boolean('Invoice Done')
    notes = fields.Text('Prescription Note')
    appointment_id = fields.Many2one('hospital.appointment')
    is_invoiced = fields.Boolean(copy=False, default=False)
    insurer_id = fields.Many2one('hospital.insurance', 'Insurer')
    is_shipped = fields.Boolean(default=False, copy=False)

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('hospital.prescription.order') or '/'
        return super(HospitalPrescriptionOrder, self).create(vals)

    def prescription_report(self):
        return self.env.ref('kmc_hospital.report_print_prescription').report_action(self)

    @api.onchange('name')
    def onchange_name(self):
        ins_obj = self.env['hospital.insurance']
        ins_record = ins_obj.search([('hospital_insurance_partner_id', '=', self.patient_id.patient_id.id)])
        self.insurer_id = ins_record.id or False
