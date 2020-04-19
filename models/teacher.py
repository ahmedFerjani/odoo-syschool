import random
from datetime import date

from odoo import models,fields,api
from odoo.odoo.exceptions import ValidationError


class teacher(models.Model):
    _name = 'syschool.teacher'

    teacher_id = fields.Char(string="Teacher ID")
    picture = fields.Binary()
    name = fields.Char(string="Full Name")

    ed_class = fields.Many2many('syschool.class', string="Responsibility of Academic Class")
    ed_course = fields.Many2many('syschool.course', string="Course-Subjects")

    po_department = fields.Char(string="Department")
    po_job = fields.Char(string="Job Position")
    po_manager = fields.Char(string="Manager")
    po_coach = fields.Char(string="Coach")


    birthdate = fields.Date(string="Birth date")
    age = fields.Char(string="Age", help="Age in years", readonly = True)

    sex = fields.Selection((('m', 'Male'), ('f', 'Female')),
                     'Sex')
    maritual_status = fields.Selection((('si', 'Single'), ('m', 'Married/Remarried'), ('se', 'Separated'), ('d', 'Divorsed')),
                     'Maritual Status')


    ad_postal = fields.Char(string="Postal Code")
    ad_city = fields.Char(string="City")
    ad_state = fields.Char(string="State Adress")
    ad_street = fields.Char(string="Street Adress")

    c_tel1 = fields.Char(string="Work Mobile")
    c_tel2 = fields.Char(string="Personal Mobile")
    c_email = fields.Char(string="Work E_mail", help="Electronic Mail")

    d_cin = fields.Binary(string="CIN", help="Copy Of CIN")
    cin = fields.Char(string="Identification No", help="CIN Number")
    d_passport = fields.Binary(string="Passport", help="Copy Of Passport")
    passport = fields.Char(string="Passport No", help="Passport Number")
    notes = fields.Text(string="other information")


    @api.onchange('birthdate')
    def set_age(self):
        if self.birthdate:
            self.age = int(date.today().strftime("%Y")) - int(self.birthdate.strftime("%Y"))


    @api.constrains('birthdate')
    def check_age(self):
        '''Method to check age available or not'''
        age  = int(date.today().strftime("%Y")) - int(self.birthdate.strftime("%Y"))
        if (age<22):
            #raise ValidationError(self.age)
            raise ValidationError("Age of Teacher should be greater than 22 years ! ")

