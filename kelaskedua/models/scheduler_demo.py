# -*- coding: utf-8 -*-
from openerp import models, fields, api
#Import logger
import logging
#Get the logger
_logger = logging.getLogger(__name__)

#External import
import datetime

class Scheduler_demo(models.Model):
    _name = 'scheduler.demo'
    name = fields.Char(required=True)
    numberOfUpdates = fields.Integer('Number of updates', help='The number of times the scheduler has run and updated this field')
    lastModified = fields.Date('Last updated')

    #This function is called when the scheduler goes off
    def process_demo_scheduler_queue(self, cr, uid, context=None):
        return {'value':{},'warning':{'title':'Hello','message':'The winter is coming'}}