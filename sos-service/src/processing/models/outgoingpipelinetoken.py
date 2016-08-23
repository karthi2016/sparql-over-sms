from processing.models import PipelineToken, OUTGOING_TOKEN


class OutgoingPipelineToken(PipelineToken):

    def __init__(self, message):
        super().__init__(message, OUTGOING_TOKEN)
