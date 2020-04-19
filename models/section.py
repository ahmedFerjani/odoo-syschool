from odoo import models, fields, api

class Section(models.Model):
    _name = 'syschool.section'

    code = fields.Char(string="Section Code")
    name = fields.Char(string="Name")

    desc = fields.Text(string="Description")
    picture = fields.Binary(string="Picture")