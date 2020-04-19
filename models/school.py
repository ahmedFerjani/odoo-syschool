from odoo import models, fields, api

class School(models.Model):
    _name = 'syschool.school'

    logo = fields.Binary(string="Logo")

    name = fields.Char(string="Name")

    c_tel1 = fields.Char(string="Mobile 1")
    c_tel2 = fields.Char(string="Mobile 2")
    c_fax = fields.Char(string="FAX")
    c_email = fields.Char(string="e_mail", help="Electronic Mail")

    ad_postal = fields.Char(string="Postal Code")
    ad_city = fields.Char(string="City")
    ad_state = fields.Char(string="State Adress")
    ad_street = fields.Char(string="Street Adress")