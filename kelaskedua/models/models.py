# -*- coding: utf-8 -*-

from openerp import models, fields, api

class topik(models.Model):
    _name = 'kelaskedua.topik'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)
    kelas_ids = fields.One2many(
        'kelaskedua.kelas', 'topik_id', string="Kelas")

class kelas(models.Model):
    _name = 'kelaskedua.kelas'

    name = fields.Char(string="Kelas",required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6,2),help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    topik_id = fields.Many2one('kelaskedua.topik',
        ondelete='cascade', string="Topik", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")