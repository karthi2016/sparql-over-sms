import time

import repositories
from flask import request
from injector import inject
from pipelines import SendSparqlQuery, SendSparqlUpdate
from pipelines.wrappers import PipelineToken
from pipelines.wrappers.pipelinetoken import OUTGOING_TOKEN
from transfer.messenger import MSG_SPARQL_QUERY, MSG_SPARQL_UPDATE, MSG_SPARQL_QUERY_RESPONSE
from transfer.wrappers.message import Message
from webapi import app
from webapi.helpers.crossdomain import crossdomain
from webapi.helpers.responses import *
from timeit import default_timer as timer


@crossdomain()
@inject(contactrepo=repositories.ContactRepo)
@app.route('/query/endpoints', methods=['GET', 'OPTIONS'])
def get_queryendpoints(contactrepo):
    contacts = [c for c in contactrepo.get_contacts() if c['sparqlenabled'] == 'yes']

    endpoints = []
    for contact in contacts:
        endpoint = {
            'contact': contact['fullname'],
            'sparql': {
                'query': '/query/{0}/sparql'.format(contact['contactid']),
                'update': '/query/{0}/sparql/update'.format(contact['contactid'])
            }
        }
        endpoints.append(endpoint)

    return ok(endpoints)


@crossdomain()
@app.route('/query/<contactid>/sparql', methods=['GET', 'OPTIONS'])
@inject(messagerepo=repositories.MessageRepo)
def outgoing_sparql(contactid, messagerepo):
    query = request.args.get('query')

    # send sparql query to contact
    message = Message(MSG_SPARQL_QUERY, query, receiver=contactid)
    result = SendSparqlQuery.execute(PipelineToken(message, OUTGOING_TOKEN))
    print('SendSparqlQuery: {0}'.format(result))

    # poll messages for response
    correlationid = message.correlationid
    reply = None

    started = timer()
    while reply is None:
        reply = messagerepo.find_message(correlationid, MSG_SPARQL_QUERY_RESPONSE)

        # stop if timeout is reached
        elapsed = timer() - started
        if elapsed > 30:
            break

        print('looking for {0}-{1}'.format(correlationid, MSG_SPARQL_QUERY_RESPONSE))
        time.sleep(1)

    if reply is None:
        return timeout()
    else:
        print(reply)
        return ok(reply.body)


@crossdomain()
@app.route('/query/<contactid>/sparql/update', methods=['POST', 'OPTIONS'])
def outgoing_sparqlupdate(contactid):
    update = request.form.get('update')

    # send sparql update to contact
    message = Message(MSG_SPARQL_UPDATE, update, receiver=contactid)
    result = SendSparqlUpdate.execute(PipelineToken(message, OUTGOING_TOKEN))

    print(result)
    return accepted()









