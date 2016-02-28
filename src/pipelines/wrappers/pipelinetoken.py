from pipelines.wrappers import PipelineReport


class PipelineToken:
    """Represents the instance that goes through a pipeline"""

    def __init__(self, message):
        self.original = message
        self.message = message
        self.report = PipelineReport()
        self.result = None

    def __str__(self):
        return self.result.__str__()
