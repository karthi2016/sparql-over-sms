
class HttpTransfer:
    """Transfers messages with HTTP"""
    max_bodysize = 140000

    @staticmethod
    def send_single(hostname, body):
        raise NotImplementedError('Sending messages via http')

    @staticmethod
    def send_multiple(messages):
        raise NotImplementedError('Sending multiple messages via http')

    @staticmethod
    def is_supported(receiver):
        return receiver['hostname'] is not None

