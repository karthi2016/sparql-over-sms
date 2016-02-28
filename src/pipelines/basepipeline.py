from timeit import default_timer as timer

from pipelines.wrappers import PipelineToken


class BasePipeline:
    """Base class for pipelines"""
    chain = None

    def handle(self, message):
        token = PipelineToken(message)

        for link in self.chain:
            self.execute(link, token)

        print('Total time: {0:5f}s'.format(token.report.get_totaltime()))
        return token

    def execute(self, link, token):
        # capture start time
        started = timer()

        link.execute(token)

        # calculate elapsed time
        finished = timer()
        elapsed = finished - started

        # record execution
        token.report.add_record(link.name, link.description, elapsed)

