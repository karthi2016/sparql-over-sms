import repositories

from injector import inject
from webapi import app
from webapi.helpers.responses import *


@inject(messagerepo=repositories.MessageRepo)
@app.route('/messages', methods=['GET'])
def retreive_messages(messagerepo):
    messages = messagerepo.get_messages()

    return ok(messages)


@inject(messagerepo=repositories.MessageRepo)
@app.route('/message/<messageid>', methods=['GET'])
def retreive_message(messageid, messagerepo):
    message = messagerepo.get_contact(messageid)

    return ok(message)
