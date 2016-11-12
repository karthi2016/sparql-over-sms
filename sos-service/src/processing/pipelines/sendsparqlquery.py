from processing.actions.sendmessage import SendMessage
from processing.pipelines.basepipeline import Pipeline


class SendSparqlQuery(Pipeline):
    """Pipeline that handles outgoing SPARQL queries"""
    name = 'SendSparqlQuery'
    description = 'Pipeline that handles outgoing SPARQL queries'

    chain = [
        SendMessage
    ]

    def __init__(self, token):
        self.token = token

    def execute(self):
        return Pipeline.handle(self.chain, self.token)
