from processing import celery
from persistence import message_repo
from processing.pipelines import DecompressMessage
from transfer.constants.messagecategory import MessageCategory
from processing.pipelines import ReceiveSparqlQuery, ReceiveSparqlUpdate
from processing.models import IncomingPipelineToken


@celery.task
def process_incomingmessage(messageid):
    message = message_repo.get_byid(messageid)
    token = IncomingPipelineToken(message)

    DecompressMessage.execute(token)

    # call appropriate pipeline based on category
    if message.category is MessageCategory.SPARQL_QUERY:
        token = ReceiveSparqlQuery(token).execute()

    if message.category is MessageCategory.SPARQL_UPDATE:
        token = ReceiveSparqlUpdate(token).execute()

    return token
