from flask import request
from pipelines import SendSparqlQuery, SendSparqlUpdate
from pipelines.wrappers import PipelineToken
from pipelines.wrappers.pipelinetoken import OUTGOING_TOKEN
from transfer.messenger import MSG_SPARQL_QUERY, MSG_SPARQL_UPDATE
from transfer.wrappers import Message
from webapi import app
from webapi.helpers.responses import *


@app.route('/agent/<contactid>/sparql', methods=['GET'])
def endpoint_sparql(contactid):
    query = request.args.get('query')

    try:
        message = Message(MSG_SPARQL_QUERY, query, receiver=contactid)
        result = SendSparqlQuery.execute(PipelineToken(message, OUTGOING_TOKEN))
    except TimeoutError:
        return timeout()
    except Exception as e:
        print(e)
        return servererror()

    return ok(result.message.body.lower().replace("'", "\""), 'application/sparql-results+json; charset=UTF-8')


@app.route('/agent/<contactid>/sparql/update', methods=['POST'])
def endpoint_sparqlupdate(contactid):
    update = request.form.get('update')

    try:
        message = Message(MSG_SPARQL_UPDATE, update, receiver=contactid)
        result = SendSparqlUpdate.execute(PipelineToken(message, OUTGOING_TOKEN))
    except TimeoutError:
        return timeout()
    except Exception:
        return servererror()

    return ok(result.message.body.lower().replace("'", "\""), 'application/sparql-results+json; charset=UTF-8')


