from processing.pipelines.basepipeline import Pipeline
from processing.filters import Base64Encode, GzipCompress


class SendSparqlUpdate(Pipeline):
    """Pipeline that handles outgoing SPARQL updates"""
    name = 'SendSparqlUpdate'
    description = 'Pipeline that handles outgoing SPARQL updates'

    chain = [
        GzipCompress,
        Base64Encode
    ]

    def __init__(self, token):
        self.token = token

    def execute(self):
        return Pipeline.handle(self.chain, self.token)
