# -*- coding: utf-8 -*-
{
    'name': "syschool",

    'summary': """
        A School Management System""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ferjani Ahmed",
    'website': "http://www.issatso.rnu.tn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'School Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/student.xml',
        'views/teacher.xml',
        'views/section.xml',
        'views/education.xml',
        'views/school.xml',
        'views/classroom.xml',
        'views/course.xml',
        'views/academic.xml',
        'views/rootmenu.xml',

        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}