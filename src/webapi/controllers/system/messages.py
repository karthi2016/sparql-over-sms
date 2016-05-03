import repositories
from injector import inject
from webapi import app
from webapi.helpers.responses import *


@inject(messagerepo=repositories.MessageRepo)
@app.route('/messages')
def messages(messagerepo):
    return ok([m.__dict__ for m in messagerepo.get_messages()])
