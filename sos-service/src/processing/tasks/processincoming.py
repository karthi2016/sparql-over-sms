from processing import celery
from persistence import message_repo, messaging_uow
from processing.pipelines import DecompressMessage
from transfer.constants.messagecategory import MessageCategory
from processing.pipelines import ReceiveSparqlQuery, ReceiveSparqlUpdate
from processing.models import IncomingPipelineToken
from processing.tasks.processoutgoing import  process_outgoingmessage


@celery.task
def process_incomingmessage(messageid):
    message = message_repo.get_byid(messageid)
    token = IncomingPipelineToken(message)

    DecompressMessage.execute(token)

    # call appropriate pipeline based on category
    if message.category is MessageCategory.SPARQL_QUERY:
        token = ReceiveSparqlQuery.execute(token)

        # create and send result message
        correlationid = message.correlationid
        receiveraddress = message.sender.hostname
        category = MessageCategory.SPARQL_QUERY_RESPONSE
        body = token.result
        position = 0
        resultmessage = messaging_uow.store_outgoing(receiveraddress, correlationid, category, position, body)

        process_outgoingmessage.delay(resultmessage.id)

    if message.category is MessageCategory.SPARQL_UPDATE:
        token = ReceiveSparqlUpdate.execute(token)

    return token
