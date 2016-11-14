from persistence import messaging_uow
from utilities.messaging import to_response_category
from processing.tasks.processoutgoing import process_outgoingmessage


class CreateResponse:
    """Creates a response message"""
    name = "CreateResponse"
    description = "Creates a response message"

    @staticmethod
    def execute(token):
        message = token.message

        # create and send result message
        correlationid = message.correlationid
        receiveraddress = message.sender.hostname
        category = to_response_category(message.category)
        body = token.result
        resultmessage = messaging_uow.store_outgoing(receiveraddress, correlationid, category, body)

        process_outgoingmessage.delay(resultmessage.id)
