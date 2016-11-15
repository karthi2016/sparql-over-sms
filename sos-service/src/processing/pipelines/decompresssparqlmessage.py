from processing.actions import UpdateMessage
from processing.filters import SparqlDecompress
from processing.pipelines.basepipeline import Pipeline
from processing.filters import Base64Decode, GzipDecompress


class DecompressSparqlMessage(Pipeline):
    """Decompress an incomming SPARQL-query message"""
    name = 'DecompressMessage'
    description = 'Decompress an incomming SPARQL-query message'

    chain = [
        Base64Decode,
        GzipDecompress,
        SparqlDecompress,
        UpdateMessage
    ]

    def __init__(self, token):
        self.token = token

    def execute(self):
        return Pipeline.handle(self.chain, self.token)
