from base64 import b64decode


class Base64Decode:
    """Performs Base64 decoding"""
    name = "Base64Decode"
    description = "Performs Base64 decoding"

    @staticmethod
    def execute(token):
        message = token.message
        body = message.get_body()

        # re-assign decoded body
        b64body = body.replace('_', '+').replace('-', '=').replace(',', '/')
        token.message.body = b64decode(b64body)
