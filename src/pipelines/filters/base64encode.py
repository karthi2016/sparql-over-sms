from base64 import b64encode


class Base64Encode:
    """Performs Base64 encoding"""
    name = "Base64Encode"
    description = "Performs Base64 encoding"

    @staticmethod
    def execute(token):
        token.message.body = b64encode(str.encode(token.message.body)).decode('utf-8')
