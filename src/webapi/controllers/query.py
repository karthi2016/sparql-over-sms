import repositories

from flask import request
from injector import inject
from pipelines import SendSparqlQuery, SendSparqlUpdate
from pipelines.wrappers import PipelineToken
from pipelines.wrappers.pipelinetoken import OUTGOING_TOKEN
from transfer.messenger import MSG_SPARQL_QUERY, MSG_SPARQL_UPDATE
from transfer.wrappers import Message
from webapi import app
from webapi.helpers import crossdomain
from webapi.helpers.responses import *


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
def outgoing_sparql(contactid):
    query = request.args.get('query')

    try:
        message = Message(MSG_SPARQL_QUERY, query, receiver=contactid)
        result = SendSparqlQuery.execute(PipelineToken(message, OUTGOING_TOKEN))
    except TimeoutError:
        return timeout()
    except Exception:
        return servererror()

    return ok(result.message.body.lower().replace("'", "\""))


@crossdomain()
@app.route('/query/<contactid>/sparql/update', methods=['POST', 'OPTIONS'])
def outgoing_sparqlupdate(contactid):
    update = request.form.get('update')

    try:
        message = Message(MSG_SPARQL_UPDATE, update, receiver=contactid)
        result = SendSparqlUpdate.execute(PipelineToken(message, OUTGOING_TOKEN))
    except TimeoutError:
        return timeout()
    except Exception:
        return servererror()
    
    return ok(result.message.body.lower().replace("'", "\""))









