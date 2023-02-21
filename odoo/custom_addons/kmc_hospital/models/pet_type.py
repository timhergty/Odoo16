from odoo import api, fields, models, _


class PetType(models.Model):
    _name = 'pet.type'
    _description = 'pet type'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code')
