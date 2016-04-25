from pipelines.wrappers import PipelineReport

INCOMING_TOKEN = 0
OUTGOING_TOKEN = 1


class PipelineToken:
    """Represents the instance that goes through a pipeline"""

    def __init__(self, message, category):
        self.category = category
        self.report = PipelineReport()
        self.result = None

        # use the provided message as working item
        self.message_original = message
        self.message = message

        # this will be used when converted from incoming to outgoing
        self.replyto_original = None
        self.replyto = None

    def __str__(self):
        return self.message.__str__()
