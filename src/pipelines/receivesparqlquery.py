from pipelines.actions import RunSparqlQuery
from pipelines.basepipeline import Pipeline
from pipelines.filters import Base64Decode, ToResponse
from pipelines.sendsparqlresponse import SendSparqlResponse


class ReceiveSparqlQuery(Pipeline):
    """Pipeline that handles incoming SPARQL queries"""
    name = 'ReceiveSparqlQuery'
    description = 'Pipeline that handles incoming SPARQL queries'

    chain = [
        Base64Decode,
        RunSparqlQuery,
        ToResponse,
        SendSparqlResponse
    ]

    @staticmethod
    def execute(token):
        return Pipeline.handle(ReceiveSparqlQuery.chain, token)
