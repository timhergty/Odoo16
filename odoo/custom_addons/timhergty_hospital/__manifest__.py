{

    "name": "Hospital Management System (HMS)",
    "version": "1.8.7",
    "currency": 'UGX',
    "summary": """
    Manage day to day operations of the Hospital
    """,
    "category": "Industries",
    "sequence": '-120',
    "license": "LGPL-3",
    "description": """
    Healthcare Management Clinic Management apps manage clinic manage Patient hospital 
    manage Healthcare system Patient Management Hospital Management Healthcare Management 
    Clinic Management hospital Lab Test Request
    Techthings developed a new odoo/OpenERP module apps
    This module is used to manage Hospital and Healthcare Management and Clinic Management apps. 
    manage clinic manage Patient hospital in odoo manage Healthcare system Patient Management, 
    Odoo Hospital Management odoo Healthcare Management Odoo Clinic Management
    Odoo hospital Patients
    Odoo Healthcare Patients Card Report
    Odoo Healthcare Patients Medication History Report
    Odoo Healthcare Appointments
    Odoo hospital Appointments Invoice
    Odoo Healthcare Families Prescriptions Healthcare Prescriptions
    Odoo Healthcare Create Invoice from Prescriptions odoo hospital Prescription Report
    Odoo Healthcare Patient Hospitalization
    odoo Hospital Management System
    Odoo Healthcare Management System
    Odoo Clinic Management System
    Odoo Appointment Management System
    health care management system
    Generate Report for patient details, appointment, prescriptions, lab-test

    Odoo Lab Test Request and Result
    Odoo Patient Hospitalization details
    Generate Patient's Prescriptions

    
""",

    "depends": ["base", "sale_management", "stock", "account", "board", 'website'],
    "data": [
        'security/hospital_groups.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/assets.xml',
        'views/login_page.xml',
        'views/main_menu_file.xml',
        'wizard/appointments_invoice_wizard.xml',
        'wizard/create_prescription_invoice_wizard.xml',
        'wizard/create_prescription_shipment_wizard.xml',
        'views/medicament.xml',
        'views/drug_route.xml',
        'wizard/lab_test_create_wizard.xml',
        'wizard/lab_test_invoice_wizard.xml',
        'views/prescription_order.xml',
        'views/directions.xml',
        'views/dose_unit.xml',
        'views/patient_ovulation.xml',
        'views/family_disease.xml',
        'views/inpatient_registration.xml',
        'views/inpatient_medication.xml',
        'views/insurance_plan.xml',
        'views/appointment.xml',
        'views/insurance.xml',
        'views/patient_lab_test.xml',
        'views/lab_test_units.xml',
        'views/lab.xml',
        'views/dashboard.xml',
        'views/template.xml',
        'views/portal_template.xml',
        'views/neomatal_apgar.xml',
        'views/pathology_category.xml',
        'views/pathology_group.xml',
        'views/pathology.xml',
        'views/patient_disease.xml',
        'views/patient_medication.xml',
        'views/patient_medication1.xml',
        'views/patient_pregnancy.xml',
        'views/patient_perinatal_ovulation.xml',
        'views/patient.xml',
        'views/physician.xml',
        'views/perinatal.xml',
        'views/prescription_line.xml',
        'views/puerperium_monitor.xml',
        'views/rcri.xml',
        'views/rounding_procedure.xml',
        'views/test_criteria.xml',
        'views/test_type.xml',
        'views/vaccination.xml',
        'views/res_partner.xml',
        'report/report_view.xml',
        'report/appointment_receipts_report_template.xml',
        'report/view_report_document_lab.xml',
        'report/view_report_lab_result_demo_report.xml',
        'report/newborn_card_report.xml',
        'report/patient_card_report.xml',
        'report/patient_diseases_document_report.xml',
        'report/patient_medications_document_report.xml',
        'report/patient_vaccinations_document_report.xml',
        'report/prescription_demo_report.xml',
    ],
    "author": "Timothy Wasike",
    "website": "https://www.techthings.it",
    "installable": True,
    "application": True,
    "auto_install": False,
    "images": ["static/description/Banner.gif"],
    "live_test_url": '#',

}
