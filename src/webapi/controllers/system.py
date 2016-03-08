import repositories

from injector import inject
from webapi import app
from webapi.helpers.responses import *


@app.route('/')
def get_status():
    return ok({'name': 'Semantic M2M', 'version': '0.0.0'})


@app.route('/messages')
@inject(messagerepo=repositories.MessageRepo)
def messages(messagerepo):
    return ok(messagerepo.get_messages())


@app.route('/message/<messageid>')
@inject(messagerepo=repositories.MessageRepo)
def message(messageid, messagerepo):
    return ok(messagerepo.get_message(messageid))


@app.route('/addmessage')
@inject(messagerepo=repositories.MessageRepo)
def addmessage(messagerepo):
    messagerepo.add_message('corr', '1', 'machine01', 'bodybodb')

    return ok({'ok': 'ok'})






