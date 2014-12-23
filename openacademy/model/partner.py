# -*- coding: utf-8 -*-
from openerp import fields, models

class Partner(models.Model):
	_inherit = 'res.partner'

	# Le agrego una nueva columna al modelo res.partner, por defecto los partner
	# no son instructores
	instructor = fields.Boolean("Instructor", default=False)	
	session_ids = fields.Many2many('openacademy.session',
									string="Attended Sessions", readonly=True)