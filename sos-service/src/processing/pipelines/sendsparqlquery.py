from processing.pipelines.basepipeline import Pipeline
from processing.filters import Base64Encode, ToResponse, GzipCompress
from processing.actions import SendResponse, AwaitResponse


class SendSparqlQuery(Pipeline):
    """Pipeline that handles outgoing SPARQL queries"""
    name = 'SendSparqlQuery'
    description = 'Pipeline that handles outgoing SPARQL queries'

    chain = [
        GzipCompress,
        Base64Encode,
        SendResponse,
        ToResponse,
        AwaitResponse
    ]

    @staticmethod
    def execute(token):
        return Pipeline.handle(SendSparqlQuery.chain, token)
