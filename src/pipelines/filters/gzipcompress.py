from io import BytesIO
from gzip import GzipFile


class GzipCompress:
    """Performs Gzip compression"""
    name = "GzipCompression"
    description = "Performs Gzip compression"

    @staticmethod
    def execute(token):
        mockfile = BytesIO()
        with GzipFile(fileobj=mockfile, mode="w") as f:
            f.write(bytes(token.message.body, 'utf-8'))

        token.message.body = mockfile.getvalue()
