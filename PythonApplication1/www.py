import datetime

from bottle import get,run,view

@get('/')
@view('modele')
def coucou():
    return {"arg":datetime.datetime.now()}

@get('/<nom>')
@view('modele')
def coucou(nom):
    return {"arg":nom.upper()}

run(host='localhost',debug=True,port=8080,reloader=True)