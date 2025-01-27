from odoo import models, fields, api

class EmpleadoBirthday(models.Model):
    #_inherit = 'hr.employee'  
    _name = 'birthday.empleado_birthday'
    _description = 'Mensaje de Cumpleaños'

    envio_mensage_birthday = fields.Boolean(
        string='Envío mensaje cumpleaños',
        help="Indicates whether a birthday message has been sent to this employee."
    )
    birthday = fields.Date(string='Cumpleaños')
    name = fields.Char(string="Nombre", required=True)

    @api.model
    def comparacion_birthdays(self):
        dia_actual = fields.Date.today()
        dia_mes_actual = dia_actual.strftime('%d-%m')

        # Buscando empleados cuyo cumpleaños coincida con el día y mes actuales
        employees = self.search([
            ('birthday', 'like', dia_mes_actual),
            ('envio_mensage_birthday', '=', False)
        ])

        for employee in employees:
            self.envio_birthday_email(employee)
            # Actualizando el campo para que no se envíen más mensajes
            employee.write({'envio_mensage_birthday': True})

    def envio_birthday_email(self, employee):
        contenido_email = self.env.ref('birthday.bdayemail')
        if contenido_email:
            # Enviando el correo
            contenido_email.send_mail(employee.id, force_send=True, email_values={
                'email_from': employee.company_id.email,
                'email_to': employee.work_email,
                'object': employee.name,  # Suponiendo que deseas el nombre del empleado como asunto
            })
            # Actualizando el campo después de enviar el correo
            employee.write({'envio_mensage_birthday': True})
