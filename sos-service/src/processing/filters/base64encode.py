from base64 import b64encode


class Base64Encode:
    """Performs Base64 encoding"""
    name = "Base64Encode"
    description = "Performs Base64 encoding"

    @staticmethod
    def execute(token):
        message = token.message
        body = message.get_body()

        # re-assign encoded body
        token.message.body = b64encode(body).decode('utf-8')
