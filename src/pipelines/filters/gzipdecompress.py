from io import BytesIO
from gzip import GzipFile


class GzipDecompress:
    """Performs Gzip decompression"""
    name = "GzipDecompression"
    description = "Performs Gzip decompression"

    @staticmethod
    def execute(token):
        mockfile = BytesIO()
        mockfile.write(token.message.body)
        mockfile.seek(0)

        with GzipFile(fileobj=mockfile, mode="r") as f:
            token.message.body = f.read().decode('utf-8')
