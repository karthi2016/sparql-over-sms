from pipelines.basepipeline import Pipeline
from pipelines.filters import Base64Decode


class ReceiveSparqlResponse(Pipeline):
    """Receives a SPARQL query/update response"""
    name = 'ReceiveSparqlResponse'
    description = 'Receives a SPARQL query/update response'

    chain = {
        Base64Decode
    }

    @staticmethod
    def execute(token):
        Pipeline.handle(ReceiveSparqlResponse.chain, token)
