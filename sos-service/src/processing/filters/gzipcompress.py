from io import BytesIO
from gzip import GzipFile


class GzipCompress:
    """Performs Gzip compression"""
    name = "GzipCompression"
    description = "Performs Gzip compression"

    @staticmethod
    def execute(token):
        message = token.message
        body = message.get_body()

        mockfile = BytesIO()
        with GzipFile(fileobj=mockfile, mode="w") as f:
            f.write(bytes(body, 'utf-8'))

        # re-assign compressed body
        token.message.body = mockfile.getvalue()
