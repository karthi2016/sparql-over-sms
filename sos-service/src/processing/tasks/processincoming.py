from processing import celery
from persistence import message_repo, messaging_uow
from processing.pipelines import DecompressSparqlMessage
from transfer.constants.messagecategory import MessageCategory
from processing.pipelines import ReceiveSparqlQuery, ReceiveSparqlUpdate
from processing.models import IncomingPipelineToken


@celery.task
def process_incomingmessage(messageid):
    message = message_repo.get_byid(messageid)
    token = IncomingPipelineToken(message)

    # call appropriate pipeline based on category
    if message.category is MessageCategory.SPARQL_QUERY:
        token = DecompressSparqlMessage(token).execute()
        token = ReceiveSparqlQuery(token).execute()

    if message.category is MessageCategory.SPARQL_UPDATE:
        token = DecompressSparqlMessage(token).execute()
        token = ReceiveSparqlUpdate(token).execute()

    messaging_uow.mark_processed(message)
    return token
