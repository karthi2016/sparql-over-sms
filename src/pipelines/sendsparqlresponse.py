from pipelines.actions import SendSms
from pipelines.basepipeline import Pipeline
from pipelines.filters import Base64Encode


class SendSparqlResponse(Pipeline):
    """Sends a SPARQL query/update response"""
    name = 'SendSparqlResponse'
    description = 'Sends a SPARQL query/update response'

    chain = {
        Base64Encode,
        SendSms
    }

    @staticmethod
    def execute(token):
        return Pipeline.handle(SendSparqlResponse.chain, token)