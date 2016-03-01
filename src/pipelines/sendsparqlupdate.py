from pipelines.basepipeline import Pipeline
from pipelines.filters import Base64Encode
from pipelines.actions import SendSms


class SendSparqlUpdate(Pipeline):
    """Pipeline that handles outgoing SPARQL updates"""
    name = 'SendSparqlUpdate'
    description = 'Pipeline that handles outgoing SPARQL updates'

    chain = [
        Base64Encode,
        SendSms
    ]

    @staticmethod
    def execute(token):
        return Pipeline.handle(SendSparqlUpdate.chain, token)
