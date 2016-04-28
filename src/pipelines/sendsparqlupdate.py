from pipelines.basepipeline import Pipeline
from pipelines.filters import Base64Encode, ToResponse, GzipCompress
from pipelines.actions import SendMessage, AwaitResponse


class SendSparqlUpdate(Pipeline):
    """Pipeline that handles outgoing SPARQL updates"""
    name = 'SendSparqlUpdate'
    description = 'Pipeline that handles outgoing SPARQL updates'

    chain = [
        GzipCompress,
        Base64Encode,
        SendMessage,
        ToResponse,
        AwaitResponse
    ]

    @staticmethod
    def execute(token):
        return Pipeline.handle(SendSparqlUpdate.chain, token)
