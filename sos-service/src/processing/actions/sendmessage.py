from transfer.strategies import HttpTransfer


class SendMessage:
    """Sends a message"""
    name = "SendMessage"
    description = "Sends a message"

    @staticmethod
    def execute(token):
        message = token.message

        # compose content
        correlationid = message.correlationid
        category = message.category
        position = 0
        body = message.get_body()
        content = "{0}{1}{2}{3}".format(correlationid, category, position, body)

        if HttpTransfer.is_supported(message.receiver):
            HttpTransfer.send_single(message.receiver, content)

