# -*- coding: utf-8 -*-

from openerp import models, fields, api

'''
This module create a Course's model
'''
class Course(models.Model):
	'''
	This class create a course's model
	'''
	_name = 'openacademy.course' # Nombre del modelo de odoo
	
	name = fields.Char(string='Title', required=True) #Campo reservado para identificar el nombre de referencia
	description = fields.Text(string='Description')
	responsible_id = fields.Many2one('res.users',
									ondelete='set null', 
									string="Responsible", index=True)
	session_ids= fields.One2many('openacademy.session', 'course_id', string="Session")