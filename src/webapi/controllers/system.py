import repositories
from injector import inject
from webapi import app
from webapi.helpers.responses import *


@app.route('/')
def get_status():
    return ok({'name': 'SPARQL over SMS', 'version': app.releaseversion})


@inject(messagerepo=repositories.MessageRepo)
@app.route('/messages')
def messages(messagerepo):
    return ok(messagerepo.get_messages())
