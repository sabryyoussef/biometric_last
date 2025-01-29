
{
    'name': 'Biometric Device Integration',
    'version': '17.0.1.2.2',
    'category': 'Human Resources',
    'summary': "test"
               "test)",
    'description': "test"
                   "test",
    'author': 'test',
    'company': 'test',
    'maintainer': 'test',
    'website': "test",
    'depends': ['base_setup', 'hr_attendance'],
    'external_dependencies': {
        'python': ['pyzk'], },
    'data': [
        'security/ir.model.access.csv',
        'views/biometric_device_details_views.xml',
        'views/hr_employee_views.xml',
        'views/daily_attendance_views.xml',
        'views/biometric_device_attendance_menus.xml',
        'data/download_data.xml'
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
