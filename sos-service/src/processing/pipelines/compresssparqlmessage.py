from processing.actions import UpdateMessage
from processing.pipelines.basepipeline import Pipeline
from processing.filters import Base64Encode, GzipCompress, SparqlCompress


class CompressSparqlMessage(Pipeline):
    """Compress an outgoing SPARQL message"""
    name = 'CompressMessage'
    description = 'Compress an outgoing message'

    chain = [
        SparqlCompress,
        GzipCompress,
        Base64Encode,
        UpdateMessage
    ]

    def __init__(self, token):
        self.token = token

    def execute(self):
        return Pipeline.handle(self.chain, self.token)
