from odoo import models, fields, api

class Class(models.Model):
    _name = 'syschool.class'

    ID = fields.Char(string="Classroom ID")
    name = fields.Char(string="Name")
    acy = fields.Many2one(comodel_name='syschool.academic', string="Academic Year", required=True)
    nbr = fields.Char(string="Number of Students")
    section = fields.Char(String="Section")
    desc = fields.Text(string="Description")
    student_ids = fields.One2many("syschool.student", "ed_class", "List of Students", readonly=True)
    teachers = fields.Char(string="List of teachers")