from transfer.models import BaseMessage


class ToResponse:
    """Converts an incoming token to an outgoing token"""
    name = 'ToResponse'
    description = 'Converts an incoming token to an outgoing token'

    @staticmethod
    def execute(token):
        replyto_original = token.message_original
        replyto = token.message

        category = replyto.category + 1
        receiver = replyto.sender
        body = '{0}'.format(token.result)
        # a new message becomes the new working item
        message = Message(category, body, receiver=receiver, correlationid=replyto.correlationid)

        from processing.models.pipelinetoken import OUTGOING_TOKEN
        token.category = OUTGOING_TOKEN

        # current message becomes the replyto
        token.replyto_original = replyto_original
        token.replyto = replyto

        # new message becomes the working item
        token.message_original = message
        token.message = message




