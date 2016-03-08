import repositories

from flask import request
from injector import inject
from pipelines import ReceiveSparqlQuery, ReceiveSparqlResponse, ReceiveSparqlUpdate
from pipelines.wrappers import PipelineToken, INCOMING_TOKEN
from transfer.messenger import MSG_SPARQL_QUERY, MSG_SPARQL_UPDATE, MSG_SPARQL_QUERY_RESPONSE, MSG_SPARQL_UPDATE_RESPONSE
from transfer import Messenger
from webapi import app
from webapi.helpers.responses import *


@inject(contactrepo=repositories.ContactRepo)
@app.route('/incoming', methods=['POST'])
def incoming(contactrepo):
    payload = request.get_json()
    sender = payload['sender']
    body = payload['body']

    # process message
    messenger = Messenger(contactrepo)
    message = messenger.receive(sender, body)

    pipeline = None
    if message.category is MSG_SPARQL_QUERY:
        pipeline = ReceiveSparqlQuery
    elif message.category is MSG_SPARQL_UPDATE:
        pipeline = ReceiveSparqlUpdate
    elif message.category in [MSG_SPARQL_QUERY_RESPONSE, MSG_SPARQL_UPDATE_RESPONSE]:
        pipeline = ReceiveSparqlResponse

    if pipeline is not None:
        pipeline.execute(PipelineToken(message, INCOMING_TOKEN))
    else:
        print('No suitable pipeline found..')

    return nocontent()
