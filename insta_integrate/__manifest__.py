# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : ' Instagram',
    'version' : '1.1',
    'summary': 'Customization',
    'sequence': 10,
    'description': """Customization in odoo modules  """,
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    'images' : ['static/description/background.png'],
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
         'views/menu.xml',
         'views/desk.xml',
         'views/token.xml',
         
        ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
