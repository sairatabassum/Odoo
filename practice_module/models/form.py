from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class PracticeFrom(models.Model):
    _name = "practice.form"
    # Adding Tracking Fields
    _inherit = ['mail.thread']
    _description = "Practice form record"

    name = fields.Char(string="Name", required=True, tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    is_child = fields.Boolean(string="Is Child?", tracking=True)
    notes = fields.Text(string="Notes", tracking=True)
    gender = fields.Selection([("male", "Male"), ("female", "Female"), ("others", "Others")], string="Gender",
                              tracking=True)
    capitalized_name = fields.Char(string=" Capitalized Name", compute="_compute_capitalized_name", store=True)
    ref = fields.Char(string="Reference", default=lambda self: _('New'))
    doctor_id = fields.Many2one('doctor.form', string='Doctor')
    tag_ids = fields.Many2many('res.partner.category', 'hospital_patient_tag_relation', 'patient_id', 'tag_id',
                               string="Tags")
    #
    # class CustomPartner(models.Model):
    #     _inherit = 'practice.form'
    #
    #     custom_field = fields.Char(string='Custom Field')

    class Doctors(models.Model):
        _name = 'doctor.line'

        name = fields.Char(string='Doctor Name', )
        doctor_id = fields.Many2one(comodel_name='practice.form', string='Practice', )


    @api.model_create_multi
    def create(self, vals_list):
        # Sequence number added
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('makehub.form')
        # Create method and make change into data & Inherit create method
        # for vals in vals_list:
        #     vals['gender'] = 'female'
        return super(PracticeFrom, self).create(vals_list)

    @api.constrains("is_child", 'age')
    def check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError("Age has to be recorded")

    @api.depends('name')
    def _compute_capitalized_name(self):
        if self.name:
            self.capitalized_name = self.name.upper()
        else:
            self.capitalized_name = ''

    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False
