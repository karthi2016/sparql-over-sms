import repositories

from base64 import b64decode
from flask import request
from injector import inject
from pipelines.receivesparqlquery import ReceiveSparqlQuery
from pipelines.receivesparqlresponse import ReceiveSparqlResponse
from pipelines.receivesparqlupdate import ReceiveSparqlUpdate
from pipelines.wrappers import PipelineToken
from pipelines.wrappers.message import Message
from pipelines.wrappers.pipelinetoken import INCOMING_TOKEN
from services.messenger import SPARQL_QUERY, SPARQL_UPDATE, SPARQL_QUERY_RESPONSE, SPARQL_UPDATE_RESPONSE
from webapi import app
from webapi.helpers.responses import *


@inject(contactrepo=repositories.ContactRepo)
@app.route('/incoming', methods=['POST'])
def incoming(contactrepo):
    payload = request.get_json()
    phonenumber = payload['sender']
    content = b64decode(payload['body']).decode('utf-8').strip()

    # process message
    category, body = content.split(' ', 1)
    sender = contactrepo.find_contact(phonenumber)

    message = Message(int(category), body, sender=sender['contactid'])
    pipeline = None
    if message.category is SPARQL_QUERY:
        pipeline = ReceiveSparqlQuery
    elif message.category is SPARQL_UPDATE:
        pipeline = ReceiveSparqlUpdate
    elif message.category in [SPARQL_QUERY_RESPONSE, SPARQL_UPDATE_RESPONSE]:
        pipeline = ReceiveSparqlResponse

    if pipeline is not None:
        token = pipeline.execute(PipelineToken(message, INCOMING_TOKEN))
        print('Total time: {0:5f}s'.format(token.report.get_totaltime()))
    else:
        print('No suitable pipeline found..')

    return accepted()
