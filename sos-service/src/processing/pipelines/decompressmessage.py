from processing.actions import UpdateMessage
from processing.pipelines.basepipeline import Pipeline
from processing.filters import Base64Decode, GzipDecompress


class DecompressMessage(Pipeline):
    """Decompress an incomming message"""
    name = 'DecompressMessage'
    description = 'Decompress an incomming message'

    chain = [
        Base64Decode,
        GzipDecompress,
        UpdateMessage
    ]

    @staticmethod
    def execute(token):
        return Pipeline.handle(DecompressMessage.chain, token)
