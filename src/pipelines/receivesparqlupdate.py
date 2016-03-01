from pipelines.actions import RunSparqlUpdate
from pipelines.basepipeline import Pipeline
from pipelines.filters import Base64Decode


class ReceiveSparqlUpdate(Pipeline):
    """Pipeline that handles incoming SPARQL updates"""
    name = 'ReceiveSparqlUpdate'
    description = 'Pipeline that handles incoming SPARQL updates'

    chain = [
        Base64Decode,
        RunSparqlUpdate
    ]

    @staticmethod
    def execute(token):
        return Pipeline.handle(ReceiveSparqlUpdate.chain, token)

