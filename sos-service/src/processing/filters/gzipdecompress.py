from io import BytesIO
from gzip import GzipFile


class GzipDecompress:
    """Performs Gzip decompression"""
    name = "GzipDecompression"
    description = "Performs Gzip decompression"

    @staticmethod
    def execute(token):
        message = token.message
        body = message.get_body()

        mockfile = BytesIO()
        mockfile.write(body)
        mockfile.seek(0)

        with GzipFile(fileobj=mockfile, mode="r") as f:
            # re-assign decompressed body
            token.message.body = f.read().decode('utf-8')