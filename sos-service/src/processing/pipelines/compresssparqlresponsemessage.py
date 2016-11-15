from processing.actions import UpdateMessage
from processing.pipelines.basepipeline import Pipeline
from processing.filters import Base64Encode, GzipCompress, SparqlResponseCompress


class CompressSparqlResponseMessage(Pipeline):
    """Compress an outgoing SPARQL-response message"""
    name = 'CompressMessage'
    description = 'Compress an outgoing message'

    chain = [
        SparqlResponseCompress,
        GzipCompress,
        Base64Encode,
        UpdateMessage
    ]

    def __init__(self, token):
        self.token = token

    def execute(self):
        return Pipeline.handle(self.chain, self.token)
