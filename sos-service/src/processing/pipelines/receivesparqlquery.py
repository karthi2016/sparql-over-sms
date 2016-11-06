from processing.actions import RunSparqlQuery
from processing.pipelines.basepipeline import Pipeline


class ReceiveSparqlQuery(Pipeline):
    """Pipeline that handles incoming SPARQL queries"""
    name = 'ReceiveSparqlQuery'
    description = 'Pipeline that handles incoming SPARQL queries'

    chain = [
        RunSparqlQuery
    ]

    @staticmethod
    def execute(token):
        return Pipeline.handle(ReceiveSparqlQuery.chain, token)
