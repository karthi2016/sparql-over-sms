from persistence import message_repo
from processing import celery
from processing.models import OutgoingPipelineToken
from processing.pipelines import CompressMessage
from processing.pipelines import SendSparqlQuery, SendSparqlQueryResponse
from processing.pipelines import SendSparqlUpdate, SendSparqlUpdateResponse
from transfer.constants import MessageCategory


@celery.task
def process_outgoingmessage(messageid):
    message = message_repo.get_byid(messageid)
    token = OutgoingPipelineToken(message)

    CompressMessage.execute(token)

    # call appropriate pipeline based on category
    if message.category is MessageCategory.SPARQL_QUERY:
        return SendSparqlQuery(token).execute()

    if message.category is MessageCategory.SPARQL_UPDATE:
        return SendSparqlUpdate(token).execute()

    if message.category is MessageCategory.SPARQL_QUERY_RESPONSE:
        return SendSparqlQueryResponse(token).execute()

    if message.category is MessageCategory.SPARQL_UPDATE_RESPONSE:
        return SendSparqlUpdateResponse(token).execute()
