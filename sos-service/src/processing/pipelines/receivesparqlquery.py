from processing.actions import RunSparqlQuery
from processing.actions.createresponse import CreateResponse
from processing.pipelines.basepipeline import Pipeline


class ReceiveSparqlQuery(Pipeline):
    """Pipeline that handles incoming SPARQL-queries"""
    name = 'ReceiveSparqlQuery'
    description = 'Pipeline that handles incoming SPARQL-queries'

    chain = [
        RunSparqlQuery,
        CreateResponse
    ]

    def __init__(self, token):
        self.token = token

    def execute(self):
        return Pipeline.handle(self.chain, self.token)
