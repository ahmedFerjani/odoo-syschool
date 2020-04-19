from odoo import models, fields, api

class Course(models.Model):
    _name = 'syschool.course'

    code = fields.Char("Code")
    name = fields.Char("Name")
    #section = fields.Char("Section")
    section = fields.Many2one("syschool.section", string="Section")
    hours = fields.Char("Hours/week")
    coef = fields.Char("coefficient")
    type = fields.Selection(
        [
            ('DS/TP/EX', 'DS/TP/EX'),
            ('DS/EX', 'DS/EX'),
            ('TP/EX', 'TP/EX'),
            ('EX', 'EX'),
        ], 'Type'
    )
    max_marks = fields.Integer("Maximum Marks")
    min_marks = fields.Integer("Minimum Marks")
    is_pratical = fields.Boolean('Is Pratical', help="Check if the course is pratical")
    desc = fields.Text("Description")
    teacher_ids = fields.Many2many('syschool.teacher', string="Teachers")