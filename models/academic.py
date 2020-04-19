from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class Academic_year(models.Model):
    _name = 'syschool.academic'

    name = fields.Char(string="Name", help='Name of Academic Year')
    code = fields.Char(string="Code", help='Code of Academic Year')
    current = fields.Boolean(string="Current")

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    month_ids = fields.One2many('syschool.month', 'year_id', 'Months',
                                help="related Academic months")

    desc = fields.Text(string="Description")


    @api.multi
    def generate_academicmonth(self):
        add_month = 1
        month_obj = self.env['syschool.month']

        for data in self:
            ds = data.start_date
            while (ds < data.end_date):
                de = ds + relativedelta(months=add_month, days=-1)
                if de>data.end_date:
                    de = data.end_date
                month_obj.create(
                    {
                        'name' : ds.strftime('%B'),
                        'code': ds.strftime('%m/%Y'),
                        'date_start': ds.strftime('%Y-%m-%d'),
                        'date_stop': de.strftime('%Y-%m-%d'),
                        'year_id': data.id,
                    }
                )
                ds = ds + relativedelta(months=add_month)
        return True


class Academic_month(models.Model):
    _name = 'syschool.month'

    name = fields.Char('Name', required=True, help='Name of Academic month')
    code = fields.Char('Code', required=True, help='Code of Academic month')
    date_start = fields.Date('Start of Period', required=True,
                             help='Starting of academic month')
    date_stop = fields.Date('End of Period', required=True,
                            help='Ending of academic month')
    year_id = fields.Many2one('syschool.academic', 'Academic Year', required=True,
                              help="Related academic year ")