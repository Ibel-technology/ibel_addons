from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    module_hr_employee_age = fields.Boolean(string='Employee Age')
    module_hr_employee_calendar_planning = fields.Boolean(string='Employee Calendar Planning')
    module_hr_employee_digitized_signature = fields.Boolean(string='Employee Digitized Signature')
    module_hr_course = fields.Boolean(string='HR Course')
   
