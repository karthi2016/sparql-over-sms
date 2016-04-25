from base64 import b64decode


class Base64Decode:
    """Performs Base64 decoding"""
    name = "Base64Decode"
    description = "Performs Base64 decoding"

    @staticmethod
    def execute(token):
        token.message.body = b64decode(str.encode(token.message.body)).decode('utf-8')
