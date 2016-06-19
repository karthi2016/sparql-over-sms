from processing.basepipeline import Pipeline
from processing.filters import Base64Encode, ToResponse, GzipCompress
from processing.actions import SendMessage, AwaitResponse


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
