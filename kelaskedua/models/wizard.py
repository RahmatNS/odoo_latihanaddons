from openerp import models, fields, api

class Wizard(models.TransientModel):
    _name = 'kelaskedua.wizard'


    def _default_kelas(self):
        return self.env['kelaskedua.kelas'].browse(self._context.get('active_id'))

    kelas_id = fields.Many2one('kelaskedua.kelas',
        string="Kelas", required=True, default=_default_kelas)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    @api.multi
    def subscribe(self):
        self.kelas_id.attendee_ids |= self.attendee_ids
        return {}