from processing.actions import RunSparqlUpdate
from processing.actions.createresponse import CreateResponse
from processing.pipelines.basepipeline import Pipeline


class ReceiveSparqlUpdate(Pipeline):
    """Pipeline that handles incoming SPARQL-updates"""
    name = 'ReceiveSparqlUpdate'
    description = 'Pipeline that handles incoming SPARQL-updates'

    chain = [
        RunSparqlUpdate,
        CreateResponse
    ]

    def __init__(self, token):
        self.token = token

    def execute(self):
        return Pipeline.handle(self.chain, self.token)

