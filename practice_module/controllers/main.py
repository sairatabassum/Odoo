from odoo import http


class MakeHubFrontend(http.Controller):

    @http.route('/form', type='http', auth='public', website=True)
    def view_form(self, **keyargs):

        record = http.request.env['practice.form'].sudo().search([])

        for rec in record:
            print("Name: ", rec.name, "Age: ", rec.age, "Gender: ", rec.gender, "Is_child: ", rec.is_child)

        return http.request.render("practice_module.make_hub_create_patient", {
            "person": record
        })

    @http.route('/thank_you', type='http', auth='public', website=True)
    def create_patient(self, **keyargs):
        # print(keyargs)

        form_result = http.request.env['practice.form'].sudo().create(
            {"name": keyargs.get("name"), "age": keyargs.get("age"), "is_child": keyargs.get('is_child'),
             "notes": keyargs.get("notes"), "gender": keyargs.get("gender")})
        return "Thanks for submitting"
