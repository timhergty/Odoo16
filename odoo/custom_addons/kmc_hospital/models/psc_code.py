from odoo import api, fields, models, _


class PscCode(models.Model):
    _name = 'psc.code'
    _description = 'psc code'

    name = fields.Char('Code', required=True)
    description = fields.Text('Long Text', required=True)
