from processing import celery
from persistence import message_repo
from transfer.constants.messagecategory import MessageCategory
from processing.pipelines import CompressMessage, DecompressMessage, ReceiveSparqlQuery, ReceiveSparqlUpdate
from processing.models import IncomingPipelineToken


@celery.task
def process_incomingmessage(messageid):
    message = message_repo.get_byid(messageid)
    token = IncomingPipelineToken(message)

    # first decompress the incoming message
    token = CompressMessage.execute(token)
    token = DecompressMessage.execute(token)

    # call appropriate pipeline based on category
    if message.category is MessageCategory.SPARQL_QUERY:
        return ReceiveSparqlQuery.execute(token)
    
    if message.category is MessageCategory.SPARQL_UPDATE:
        return ReceiveSparqlUpdate.execute(token)
