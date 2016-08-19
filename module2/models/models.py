from openerp import models, fields, api

class Artikel(models.Model):
    _name = 'blog.artikel'

    name = fields.Char(string="Judul Artikel", required=True)
    description = fields.Text(string="Isi Artikel")
    img_url = fields.Char(string="URL Gambar")