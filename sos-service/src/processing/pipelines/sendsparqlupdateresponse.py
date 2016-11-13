from processing.actions.sendmessage import SendMessage
from processing.pipelines.basepipeline import Pipeline


class SendSparqlUpdateResponse(Pipeline):
    """Pipeline that handles outgoing SPARQL-update responses"""
    name = 'SendSparqlQuery'
    description = 'Pipeline that handles outgoing SPARQL-update responses'

    chain = [
        SendMessage
    ]

    def __init__(self, token):
        self.token = token

    def execute(self):
        return Pipeline.handle(self.chain, self.token)
