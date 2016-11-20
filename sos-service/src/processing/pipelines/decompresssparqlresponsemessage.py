from processing.actions import UpdateMessage
from processing.pipelines.basepipeline import Pipeline
from processing.filters import Base64Decode, GzipDecompress, SparqlResponseDecompress


class DecompressSparqlResponseMessage(Pipeline):
    """Decompress an incoming SPARQL-response message"""
    name = 'CompressMessage'
    description = 'Decompress an incoming SPARQL-response message'

    chain = [
        Base64Decode,
        GzipDecompress,
        SparqlResponseDecompress,
        UpdateMessage
    ]

    def __init__(self, token):
        self.token = token

    def execute(self):
        return Pipeline.handle(self.chain, self.token)
