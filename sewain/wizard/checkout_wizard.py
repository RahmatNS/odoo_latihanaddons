from openerp import models,fields,api
class Checkout_wizard(models.TransientModel):
    _name = 'sewain.checkout_wizard'
    _inherit = ['mail.thread']

    def _get_peminjaman_id(self):
        active_ids = self._context.get('active_ids')
        if active_ids:
            return [(6, 0, active_ids)]
        return False

    peminjaman_ids = fields.Many2many('sewain.peminjaman', 'peminjaman_wizard_rel', 'peminjaman_id', 'wizard_id', string="Peminjaman",default=_get_peminjaman_id)
    total_harga = fields.Integer(string="Total Harga", store=True,
        compute='_get_total_harga')
    
    @api.depends('peminjaman_ids.sub_total', 'peminjaman_ids')
    def _get_total_harga(self):
        for r in self:
            for s in r.peminjaman_ids:
                r.total_harga += s.sub_total


    @api.multi
    def checkout(self):
        peminjaman = self.env['sewain.peminjaman'].browse(self._context.get('active_ids', []))
        if peminjaman:
            trans_obj = self.env['sewain.transaksi']
            _peminjaman_list = []
            for r in peminjaman:
                _peminjaman_list.append((0, 0,
                    {
                    'item_id': r.item_id.id,
                    'item_name': r.item_name,
                    'kuantitas' : r.kuantitas,
                    'waktu_mulai' : r.waktu_mulai,
                    'durasi' : r.durasi,
                    'harga_dasar' : r.harga_dasar
                    }))
            invoice = trans_obj.create({
                'peminjaman_ids': _peminjaman_list,
                'total_harga' : self.total_harga
                })
            self._send_email(invoice)
            return invoice

    @api.multi
    def _send_email(self,invoice):

        template_id = self.env['ir.model.data'].get_object_reference('sewain', 'email_template_sewain_invoice')
        self.env['mail.template'].browse(template_id[1]).send_mail(invoice.id, force_send=True)
        # return {'type': 'ir.actions.act_window_close'}
        # return template.send_mail(self.id, force_send=True)
        print self.env.uid
        # temp = self.env.ref('sewain.email_template_sewain_invoice')
        # return temp.send_mail(self.env.uid, force_send=True)