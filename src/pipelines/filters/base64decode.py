from base64 import b64decode


class Base64Decode:
    """Performs Base64 decoding"""

    @staticmethod
    def execute(message):
        message.body = b64decode(str.encode(message.body)).decode('utf-8')
        return message
