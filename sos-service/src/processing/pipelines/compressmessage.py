from processing.actions import UpdateMessage
from processing.pipelines.basepipeline import Pipeline
from processing.filters import Base64Encode, GzipCompress


class CompressMessage(Pipeline):
    """Compress an outgoing message"""
    name = 'CompressMessage'
    description = 'Compress an outgoing message'

    chain = [
        GzipCompress,
        Base64Encode,
        UpdateMessage
    ]

    @staticmethod
    def execute(token):
        return Pipeline.handle(CompressMessage.chain, token)
