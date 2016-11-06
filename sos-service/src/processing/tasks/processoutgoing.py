from persistence import message_repo
from processing import celery
from processing.models import OutgoingPipelineToken
from processing.pipelines import SendSparqlQuery
from processing.pipelines import SendSparqlUpdate
from transfer.constants import MessageCategory


@celery.task()
def process_outgoingmessage(messageid):
    message = message_repo.get_byid(messageid)
    token = OutgoingPipelineToken(message)

    # call appropriate pipeline based on category
    if message.category is MessageCategory.SPARQL_QUERY:
        return SendSparqlQuery(token).execute()

    if message.category is MessageCategory.SPARQL_UPDATE:
        return SendSparqlUpdate(token).execute()
