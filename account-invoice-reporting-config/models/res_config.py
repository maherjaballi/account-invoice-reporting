# -*- coding: utf-8 -*-
import openerp
from openerp import api, fields, models, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    module_account_invoice_comment_template = fields.Boolean(string='Account Invoice Comment Template',
        help='Adds comments on invoices. \n'
              'The comments can be edited directly on the invoices or loaded from \n'
              'templates. \n'
              'Two positions are available for the comments: \n'
              '- before invoice lines \n'
              '- after invoice lines \n'
             '-This installs the module account_invoice_comment_template.')
    
    module_account_invoice_line_report = fields.Boolean(string='Account Invoice Line Report',
        help='This module creates a new view to manage invoice lines information. \n')

    module_account_invoice_report_due_list = fields.Boolean(string='Account Invoice Report Due List',
        help='This module extends the invoice report for adding information about the \n'
              'corresponding due dates and amounts. \n')

    module_account_invoice_report_hide_line = fields.Boolean(string='Account Invoice Report Hideline',
        help='In some service companies, the customer is invoiced for a service that may consume inventory items.\n '
              'Those inventory items needs to be invoiced to account in the cost of services sold and reconcile the value\n '
              'of the inventory items delivered and sitting in the  \nUn-Invoiced Goods Delivered,\n'
              'but they should not appear to the customer on the PDF report of their invoice. \n'
              'This module allows you to hide invoice lines from the PDF report if the unit price is 0. \n'
             '-This installs the module account_invoice_report_hide_line.')


    module_base_comment_template = fields.Boolean(string='Base Comment Template',
        help='Add a new model to define templates of comments to print on documents. \n'
            'Two positions are available for the comments: \n'
            '* above document lines \n'
            '* below document lines \n'
            'This module is the base module for following modules: \n'
            '* sale_comment_template \n'
            '* purchase_comment_template \n'
            '* invoice_comment_template \n'
             '-This installs the module base_comment_template .')

    module_partner_time_to_pay = fields.Boolean(string='Partner Time to Pay',
        help='This module displays statistics related to the receivables and payables behavior of a partner  \n'
              'on the Accounting tab of the partner form view. \n'
            '-This installs the module partner_time_to_pay .')

    