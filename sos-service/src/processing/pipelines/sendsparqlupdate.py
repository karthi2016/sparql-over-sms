from processing.actions.sendmessage import SendMessage
from processing.pipelines.basepipeline import Pipeline


class SendSparqlUpdate(Pipeline):
    """Pipeline that handles outgoing SPARQL updates"""
    name = 'SendSparqlUpdate'
    description = 'Pipeline that handles outgoing SPARQL updates'

    chain = [
        SendMessage
    ]

    def __init__(self, token):
        self.token = token

    def execute(self):
        return Pipeline.handle(self.chain, self.token)
