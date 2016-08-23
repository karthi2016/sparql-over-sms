from persistence import message_repo
from utilities.messaging import to_response_category
from processing import process_outgoingmessage


class SendResponse:
    """Creates a response message"""
    name = 'StoreMessage'
    description = 'Stores a message'

    @staticmethod
    def execute(token):
        message = token.message

        # response message:
        senderid = '~self'
        receiverid = message.sender.id
        correlationid = message.correlationid
        category = to_response_category(message.category)
        position = 0
        body = token.result

        # store message, create processing task
        message = message_repo.create(senderid, receiverid, correlationid, category, position, body)
        process_outgoingmessage.delay(message.id)

