from transfer.strategies import HttpTransfer


class SendMessage:
    """Sends a message"""
    name = "SendMessage"
    description = "Sends a message"

    @staticmethod
    def execute(token):
        receiver = token.message.receiver

        # determine transfer strategy
        if HttpTransfer.is_supported(receiver):
            HttpTransfer.send_single(receiver, token.message.get_body())

