# -*- coding: utf-8 -*-
# Copyright 2016 Carlos Dauden <carlos.dauden@tecnativa.com>
# Copyright 2017 Vicent Cubells <vicent.cubells@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Contract Invoice Merge By Partner',
    'summary': 'This module merges same partner invoices generated by '
               'contracts',
    'version': '9.0.1.0.0',
    'category': 'Account',
    'license': 'AGPL-3',
    'author': "Tecnativa, "
              "Odoo Community Association (OCA)",
    'website': 'http://www.tecnativa.com',
    'depends': [
        'contract',
        'account_invoice_merge',
    ],
    'data': [
        'views/res_partner_view.xml',
    ],
    'installable': True,
}
