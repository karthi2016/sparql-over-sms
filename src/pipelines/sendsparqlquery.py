from pipelines.basepipeline import Pipeline
from pipelines.filters import Base64Encode
from pipelines.actions import SendSms


class SendSparqlQuery(Pipeline):
    """Pipeline that handles outgoing SPARQL queries"""
    name = 'SendSparqlQuery'
    description = 'Pipeline that handles outgoing SPARQL queries'

    chain = [
        Base64Encode,
        SendSms
    ]

    @staticmethod
    def execute(token):
        Pipeline.handle(SendSparqlQuery.chain, token)
