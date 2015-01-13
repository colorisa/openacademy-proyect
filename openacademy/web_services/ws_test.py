import functools
import xmlrpclib
HOST = 'localhost'
PORT = 8069
DB = 'Prueba'
USER = 'admin'
PASS = 'c0l0r1s4'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print "Logged in as %s (uid:%d)" % (USER,uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

# 2. Read the sessions
model = 'openacademy.session'
domain = []
method_name = 'search_read'
sessions = call(model, method_name, domain, ['name','seats', 'taken_seats'])
print "sessions", sessions

for session in sessions:
    print "Session %s (%s seats), taken seats %d" % (session['name'], session['seats'], session['taken_seats'])

method_name = 'search'
domain = [('name', '=', 'Prueba')]
course_ids = call('openacademy.course', method_name, domain)
print "course_ids",course_ids

method_name = 'create'
call('openacademy.course', method_name, {'name': 'Prueba'})

course_id = course_ids[0]
method_name = 'create'
new_sesion_id = call(model, method_name, {'name': 'Sesion from ws', 'course_id': course_id,})
print "new_sesion_id",new_session_id
	