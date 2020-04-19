import base64
from datetime import date
from odoo import models, fields, api, tools
from odoo.odoo.exceptions import ValidationError
from odoo.odoo.modules.module import get_module_resource
import random

class Student(models.Model):
    _name = 'syschool.student'

    _description = "Student information"

    name = fields.Char(string="Name", compute='_compute_name')
    student_id = fields.Char(string="Student ID")
    acy = fields.Many2one(comodel_name='syschool.academic', string="Academic Year")
    foreign = fields.Boolean(string="Foreign Student ?")
    picture = fields.Binary()
    ed_class = fields.Many2one(comodel_name='syschool.class', string="Classroom")
    ed_section = fields.Many2one(comodel_name='syschool.section', string="Section")
    ed_education = fields.Many2one(comodel_name='syschool.education', string="Education")

    fname = fields.Char(string="First Name")
    mname = fields.Char(string="Middle Name")
    lname = fields.Char(string="Last Name")
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

    c_tel1 = fields.Char(string="Mobile 1")
    c_tel2 = fields.Char(string="Mobile 2")
    c_email = fields.Char(string="e_mail", help="Electronic Mail")

    d_cin = fields.Binary(string="CIN")
    d_passport = fields.Binary(string="Passport")

    p_biography = fields.Text(string="Biography")
    p_remarks = fields.Html(string="remaks")

    state = fields.Selection([('draft', 'Draft'),
                              ('cancel', 'Cancel'),
                              ('done', 'Done'),
                              ('terminate', 'Terminate'),
                              ('alumni', 'Alumni')], 'Status', readonly=True, default="draft")


    @api.onchange('birthdate')
    def set_age(self):
        '''Method to calculate the age'''
        if self.birthdate:
            self.age = int(date.today().strftime("%Y")) - int(self.birthdate.strftime("%Y"))

    @api.constrains('birthdate')
    def check_age(self):
        '''Method to check age available or not'''
        age = int(date.today().strftime("%Y")) - int(self.birthdate.strftime("%Y"))
        if (age<5):
            #raise ValidationError(self.age)
            raise ValidationError("Age of student should be greater than 5 years ! ")



    @api.multi
    def set_alumni(self):
        '''Method to change state to alumni'''
        self.state = 'alumni'

    @api.multi
    def set_draft(self):
        '''Method to change state to draft'''
        self.state = 'draft'

    @api.multi
    def set_done(self):
        '''Method to change state to done'''
        self.state = 'done'

    @api.multi
    def set_terminate(self):
        '''Method to change state to terminate'''
        self.state = 'terminate'

    @api.multi
    def set_cancel(self):
        '''Method to change state to cancel'''
        self.state = 'cancel'

    @api.multi
    def generate_id(self):
        '''Method to Genreate student ID'''
        self.student_id = self.fname[0:2] + self.lname[0:2] + self.age + str(random.randint(0,9))

    @api.depends('student_id')
    def _compute_name(self):
        for record in self:
            record.name = record.student_id+":"+record.fname+" "+record.lname
