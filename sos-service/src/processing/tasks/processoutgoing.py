from persistence import message_repo, messaging_uow
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
        token = SendSparqlQuery(token).execute()

    if message.category is MessageCategory.SPARQL_UPDATE:
        token = SendSparqlUpdate(token).execute()

    if message.category is MessageCategory.SPARQL_QUERY_RESPONSE:
        token = SendSparqlQueryResponse(token).execute()

    if message.category is MessageCategory.SPARQL_UPDATE_RESPONSE:
        token = SendSparqlUpdateResponse(token).execute()

    messaging_uow.mark_processed(message)
    return token
