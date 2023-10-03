from odoo import api, fields, models, _


class DoctorForm(models.Model):
    _name = "doctor.form"
    # Adding Tracking Fields
    _inherit = ['mail.thread']
    _description = "Doctor form record"
    _rec_name = "ref"  # It displays rec name

    name = fields.Char(string="Name", required=True, tracking=True)
    gender = fields.Selection([("male", "Male"), ("female", "Female"), ("others", "Others")], string="Gender",
                              tracking=True)
    ref = fields.Char(string="Reference", required=True)
    # Archive and Unarchived option in odoo
    active = fields.Boolean(default=True)

    def name_get(self):
        res = []
        for rec in self:
            print(rec)
            name = f'{rec.ref} - {rec.name}'
            res.append((rec.id, name))
        return res
