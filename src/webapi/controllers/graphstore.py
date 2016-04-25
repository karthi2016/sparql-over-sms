import repositories

from flask_injector import request
from injector import inject
from pipelines import SendSparqlQuery, SendSparqlUpdate
from pipelines.wrappers import PipelineToken
from pipelines.wrappers.pipelinetoken import OUTGOING_TOKEN
from transfer.messenger import MSG_SPARQL_QUERY
from transfer.wrappers import Message
from webapi import app
from webapi.helpers import crossdomain
from webapi.helpers.responses import *


@crossdomain()
@app.route('/<contactid>/rdf-graph-store', methods=['GET', 'OPTIONS'])
def get(contactid):
    default = request.args.get('default')
    graphuri = request.args.get('graph')

    query = None
    if default is not None:
        query = 'CONSTRUCT { ?s ?p ?o } WHERE { ?s ?p ?o }'
    elif graphuri is not None:
        query = 'CONSTRUCT { ?s ?p ?o } WHERE { GRAPH <{0}> { ?s ?p ?o } }'.format(graphuri)

    if query is None:
        return badrequest()

    try:
        message = Message(MSG_SPARQL_QUERY, query, receiver=contactid)
        result = SendSparqlQuery.execute(PipelineToken(message, OUTGOING_TOKEN))
    except TimeoutError:
        return timeout()
    except Exception:
        return servererror()

    return ok(result.message.body)


@crossdomain()
@app.route('/<contactid>/rdf-graph-store', methods=['PUT', 'OPTIONS'])
def put(contactid):
    default = request.args.get('default')
    graphuri = request.args.get('graph')

    query = None
    if default is not None:
        query = 'DROP SILENT DEFAULT; INSERT DATA { ... }'
    elif graphuri is not None:
        query = 'DROP SILENT GRAPH <{0}>; INSERT DATA { GRAPH <{0}> { ... } }'.format(graphuri)

    if query is None:
        return badrequest()

    try:
        message = Message(MSG_SPARQL_QUERY, query, receiver=contactid)
        result = SendSparqlUpdate.execute(PipelineToken(message, OUTGOING_TOKEN))
    except TimeoutError:
        return timeout()
    except Exception:
        return servererror()

    return ok(result.message.body)


@crossdomain()
@app.route('/<contactid>/rdf-graph-store', methods=['DELETE', 'OPTIONS'])
def delete(contactid):
    default = request.args.get('default')
    graphuri = request.args.get('graph')

    query = None
    if default is not None:
        query = 'DROP DEFAULT'
    elif graphuri is not None:
        query = 'DROP GRAPH <{0}>'.format(graphuri)

    if query is None:
        return badrequest()

    try:
        message = Message(MSG_SPARQL_QUERY, query, receiver=contactid)
        result = SendSparqlUpdate.execute(PipelineToken(message, OUTGOING_TOKEN))
    except TimeoutError:
        return timeout()
    except Exception:
        return servererror()

    return ok(result.message.body)


@crossdomain()
@app.route('/<contactid>/rdf-graph-store', methods=['POST', 'OPTIONS'])
def post(contactid):
    default = request.args.get('default')
    graphuri = request.args.get('graph')

    query = None
    if default is not None:
        query = 'INSERT DATA { ... }'
    elif graphuri is not None:
        query = 'INSERT DATA { GRAPH <{0}> { ... } }'.format(graphuri)

    if query is None:
        return badrequest()

    try:
        message = Message(MSG_SPARQL_QUERY, query, receiver=contactid)
        result = SendSparqlUpdate.execute(PipelineToken(message, OUTGOING_TOKEN))
    except TimeoutError:
        return timeout()
    except Exception:
        return servererror()

    return ok(result.message.body)





