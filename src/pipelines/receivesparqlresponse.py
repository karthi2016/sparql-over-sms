from pipelines.actions.storemessage import StoreMessage
from pipelines.basepipeline import Pipeline
from pipelines.filters import Base64Decode, GzipDecompress


class ReceiveSparqlResponse(Pipeline):
    """Receives a SPARQL query/update response"""
    name = 'ReceiveSparqlResponse'
    description = 'Receives a SPARQL query/update response'

    chain = [
        Base64Decode,
        GzipDecompress,
        StoreMessage
    ]

    @staticmethod
    def execute(token):
        return Pipeline.handle(ReceiveSparqlResponse.chain, token)
