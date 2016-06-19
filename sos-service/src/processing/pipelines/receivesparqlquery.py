from processing.actions import RunSparqlQuery
from processing.pipelines.basepipeline import Pipeline
from processing.filters import Base64Decode, ToResponse, GzipDecompress
from processing.pipelines.sendsparqlresponse import SendSparqlResponse


class ReceiveSparqlQuery(Pipeline):
    """Pipeline that handles incoming SPARQL queries"""
    name = 'ReceiveSparqlQuery'
    description = 'Pipeline that handles incoming SPARQL queries'

    chain = [
        Base64Decode,
        GzipDecompress,
        RunSparqlQuery,
        ToResponse,
        SendSparqlResponse
    ]

    @staticmethod
    def execute(token):
        return Pipeline.handle(ReceiveSparqlQuery.chain, token)
