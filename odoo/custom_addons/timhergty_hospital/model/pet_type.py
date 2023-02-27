from odoo import api, fields, models, _


class PetType(models.Model):
    _name = 'pet.type'
    _description = 'Pet Type'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code')
