from base64 import b64encode


class Base64Encode:
    """Performs Base64 encoding"""

    @staticmethod
    def execute(message):
        message.body = b64encode(str.encode(message.body)).decode('utf-8')
        return message
