from timeit import default_timer as timer

from pipelines.wrappers import PipelineToken


class BasePipeline:
    """Base class for pipelines"""
    chain = None

    def handle(self, message):
        token = PipelineToken(message)

        for link in self.chain:
            start = timer()
            link.execute(token)
            finish = timer()

            print('Executed "{0}" in {1}'.format(link.name, finish - start))

        return token
