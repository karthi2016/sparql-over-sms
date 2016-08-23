from processing.models import PipelineToken, INCOMING_TOKEN


class IncomingPipelineToken(PipelineToken):

    def __init__(self, message):
        super().__init__(message, INCOMING_TOKEN)
