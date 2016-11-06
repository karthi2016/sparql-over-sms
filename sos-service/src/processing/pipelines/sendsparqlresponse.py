from processing.pipelines.basepipeline import Pipeline
from processing.filters import Base64Encode, GzipCompress


class SendSparqlResponse(Pipeline):
    """Pipeline that sends a SPARQL query/update response"""
    name = 'SendSparqlResponse'
    description = 'Pipeline that sends a SPARQL query/update response'

    chain = [
        GzipCompress,
        Base64Encode
    ]

    def __init__(self, token):
        self.token = token

    def execute(self):
        return Pipeline.handle(self.chain, self.token)
