from processing.actions import SendMessage
from processing.basepipeline import Pipeline
from processing.filters import Base64Encode, GzipCompress


class SendSparqlResponse(Pipeline):
    """Sends a SPARQL query/update response"""
    name = 'SendSparqlResponse'
    description = 'Sends a SPARQL query/update response'

    chain = [
        GzipCompress,
        Base64Encode,
        SendMessage
    ]

    @staticmethod
    def execute(token):
        return Pipeline.handle(SendSparqlResponse.chain, token)
