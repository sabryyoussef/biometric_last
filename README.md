# Biometric Device Integration

## Overview

This module integrates biometric devices with the HR Attendance system. It provides functionalities to manage biometric device details, track employee attendance, and generate reports.

## Features

- Integration with biometric devices.
- Employee attendance tracking.
- Daily attendance views and reports.
- User-friendly menus for device and attendance management.
- Supports external Python dependency `pyzk`.

## Technical Details

- **Module Name:** Biometric Device Integration
- **Version:** 17.0.1.2.2
- **Category:** Human Resources
- **License:** AGPL-3
- **Dependencies:** 
  - Odoo: base_setup, hr_attendance
  - Python: pyzk

## Data Files

- Security: `security/ir.model.access.csv`
- Views: 
  - `views/biometric_device_details_views.xml`
  - `views/hr_employee_views.xml`
  - `views/daily_attendance_views.xml`
  - `views/biometric_device_attendance_menus.xml`
- Data: `data/download_data.xml`
- Images: `static/description/banner.png`

## Installation

1. Ensure the dependencies are installed:
   - Odoo modules: `base_setup`, `hr_attendance`
   - Python library: `pyzk`
2. Place the module in your custom addons path.
3. Update the module list in Odoo.
4. Install the module through the Odoo interface.

## Author Information

- **Author:** Sabry Youssef
- **Contact:** 01000059085

## Maintainer


## License

This module is licensed under the AGPL-3 license.
