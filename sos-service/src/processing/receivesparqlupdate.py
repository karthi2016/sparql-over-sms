from processing.actions import RunSparqlUpdate
from processing.basepipeline import Pipeline
from processing.filters import Base64Decode, GzipDecompress


class ReceiveSparqlUpdate(Pipeline):
    """Pipeline that handles incoming SPARQL updates"""
    name = 'ReceiveSparqlUpdate'
    description = 'Pipeline that handles incoming SPARQL updates'

    chain = [
        Base64Decode,
        GzipDecompress,
        RunSparqlUpdate
    ]

    @staticmethod
    def execute(token):
        return Pipeline.handle(ReceiveSparqlUpdate.chain, token)

