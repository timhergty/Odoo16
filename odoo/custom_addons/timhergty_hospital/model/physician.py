from odoo import models, fields, api, _


class HospitalPhysician(models.Model):
    _name = "hospital.physician"
    _description = 'Hospital Physician'
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', 'Physician', required=True)
    institution_partner_id = fields.Many2one('res.partner', domain=[('is_institution', '=', True)],
                                             string='Institution')
    code = fields.Char('Id')
    info = fields.Text('Extra Info')
