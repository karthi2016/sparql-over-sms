from pipelines.actions import SendMessage
from pipelines.basepipeline import Pipeline
from pipelines.filters import Base64Encode, GzipCompress


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
