from odoo import models, fields, api


class Education(models.Model):
    _name = 'syschool.education'

    id = fields.Char(string="ID")
    name = fields.Char(string="Name")
    sys = fields.Selection([
        ('lmd', 'Licence-Master-Doctorat'),
        ('eng', 'Engineering Curriculum')
    ], 'Education system')
    grade = fields.Selection([('l', 'Licence'),
                              ('m', 'Master'), ('d', 'Doctorat'),
                              ('e', 'Engineering'), ('p', 'Preparatory')], 'Grade')

    level = fields.Integer(string="Level", readonly=True, compute='_compute_level')
    year = fields.Integer(string="year")
    dip = fields.Char(string="Diploma")
    spec = fields.Char(string="Speciality")
    desc = fields.Text(string="Description")

    @api.multi
    def _compute_level(self):
        for record in self:
            if (record.grade == 'l') or (record.grade == 'p'):
                record.level = 1
            elif record.grade == 'm' or record.grade == 'e':
                record.level = 2
            else:
                record.level = 3
