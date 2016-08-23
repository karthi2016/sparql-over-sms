from processing.actions import RunSparqlUpdate
from processing.pipelines.basepipeline import Pipeline


class ReceiveSparqlUpdate(Pipeline):
    """Pipeline that handles incoming SPARQL updates"""
    name = 'ReceiveSparqlUpdate'
    description = 'Pipeline that handles incoming SPARQL updates'

    chain = [
        RunSparqlUpdate
    ]

    @staticmethod
    def execute(token):
        return Pipeline.handle(ReceiveSparqlUpdate.chain, token)

