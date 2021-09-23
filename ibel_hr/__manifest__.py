
{
    'name': 'Ibel HR',
    'summary': 'HR features ',
    'version': '14.0',
    'category': 'Generic Modules/Human Resources',
    'author': 'Ibel technology',
    'website': 'https://ibeltechnology.com',
    'license': 'AGPL-3',
    'depends': [
        'hr',
        'hr_contract',
        'hr_contract_reference',
    ],
    'data': [
        'views/res_config_settings_views.xml',
        'report/contract_report_views.xml',
    ],
    'installable': True,
    'application': True
}
