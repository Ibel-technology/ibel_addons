from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    module_account_banking_sepa_direct_debit = fields.Boolean(string='SEPA Direct Debit')
    module_account_banking_sepa_credit_transfer = fields.Boolean(string='SEPA Credit Transfer')
