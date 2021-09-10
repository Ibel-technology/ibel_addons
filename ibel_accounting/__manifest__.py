
{
    'name': 'Ibel accounting',
    'summary': 'accounting features ',
    'version': '14.0',
    'category': 'Maintenance',
    'author': 'Ibel technology',
    'website': 'https://ibeltechnology.com',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'account_menu',
        'account_financial_report',
        'account_tax_balance',
        'account_reconciliation_widget',
        'account_reconcile_reconciliation_date',
        'account_move_base_import',
        'account_statement_import',
        'account_asset_management',
    ],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': True
}
