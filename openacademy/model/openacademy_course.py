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
	
	_sql_constraints = [
		('name_description_check',
		'CHECK(name != description)',
		"The title of the course should not be the description"),

		('name_unique',
		'UNIQUE(name)',
		"The course title must be unique"),
		]
	@api.one # api_one envia los parametros por defecto: cr, uid, id, context
	def copy(self, default=None):
		super(Course, self).copy(default)
		default = dict(default or {})

		copied_count = self.search_count(
			[('name', '=like', u"Copy of {}%".format(self.name))])
		if not copied_count:
			new_name = u"Copy of {}".format(self.name)
		else:
			new_name = u"Copy of {} ({})".format(self.name, copied_count)

		default['name'] = new_name
		return super(Course, self).copy(default)