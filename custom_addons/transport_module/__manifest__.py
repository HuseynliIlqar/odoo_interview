{
    'name': 'Transport Management',
    'version': '1.0.0',
    'summary': 'Manage transport and delivery information',
    'description': "Transport module to manage",
    'author': '`ilqar`',
    'category': 'Operations/Logistics',
    'depends': ['base', 'product', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/transport_views.xml',
    ],
    'installable': True,
    'application': True,
}
