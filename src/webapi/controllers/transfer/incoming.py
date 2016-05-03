import repositories

from flask import request
from injector import inject
from pipelines import ReceiveSparqlQuery, ReceiveSparqlResponse, ReceiveSparqlUpdate
from pipelines.wrappers import PipelineToken, INCOMING_TOKEN
from transfer.messenger import MSG_SPARQL_QUERY, MSG_SPARQL_UPDATE, MSG_SPARQL_QUERY_RESPONSE, MSG_SPARQL_UPDATE_RESPONSE
from transfer import Messenger
from webapi import app
from webapi.helpers.responses import *


@inject(contactrepo=repositories.ContactRepo, messagerepo=repositories.MessageRepo)
@app.route('/incoming', methods=['POST'])
def incoming(contactrepo, messagerepo):
    payload = request.get_json()
    sender = payload['sender']
    body = payload['body']

    # process message
    messenger = Messenger(contactrepo)
    message = messenger.receive(sender, body)

    if int(message.position) > 0:
        # store multi-part message
        messagerepo.add_message(message.correlationid, message.position, message.category, message.sender, message.body)

        # check if all parts are received
        multipart = messagerepo.get_message_byidandcategory(message.correlationid, message.category)
        if multipart is not None:
            message = messenger.receive_stored(multipart)
        else:
            return accepted()

    pipeline = None
    if message.category is MSG_SPARQL_QUERY:
        pipeline = ReceiveSparqlQuery
    elif message.category is MSG_SPARQL_UPDATE:
        pipeline = ReceiveSparqlUpdate
    elif message.category in [MSG_SPARQL_QUERY_RESPONSE, MSG_SPARQL_UPDATE_RESPONSE]:
        pipeline = ReceiveSparqlResponse

    if pipeline is not None:
        try:
            pipeline.execute(PipelineToken(message, INCOMING_TOKEN))
        except Exception as e:
            print(e)
    else:
        print('No suitable pipeline found..')

    return nocontent()
