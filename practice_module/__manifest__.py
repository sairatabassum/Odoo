{
    "name": "Practice Module",
    "author": "Saira Tabassum",
    "website": "www.odoomatest.tech",
    "summary": "Odoo 16 development",
    # Adding Tracking Fields
    "depends": ["base", "mail","sale"],
    "data": [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/makehubForm.xml',
        'views/doctor.xml',
        'views/create_patient.xml',


    ]
}
