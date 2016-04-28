from pipelines.basepipeline import Pipeline
from pipelines.filters import Base64Encode, ToResponse, GzipCompress
from pipelines.actions import SendMessage, AwaitResponse


class SendSparqlQuery(Pipeline):
    """Pipeline that handles outgoing SPARQL queries"""
    name = 'SendSparqlQuery'
    description = 'Pipeline that handles outgoing SPARQL queries'

    chain = [
        GzipCompress,
        Base64Encode,
        SendMessage,
        ToResponse,
        AwaitResponse
    ]

    @staticmethod
    def execute(token):
        return Pipeline.handle(SendSparqlQuery.chain, token)
