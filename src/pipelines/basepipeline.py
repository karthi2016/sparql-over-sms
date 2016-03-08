from timeit import default_timer as timer


class Pipeline:
    """Base class for pipelines"""

    @staticmethod
    def handle(chain, token):

        for link in chain:
            print(token.message)

            # capture start time
            started = timer()

            link.execute(token)

            # calculate elapsed time
            finished = timer()
            elapsed = finished - started

            # record execution
            token.report.add_record(link.name, link.description, elapsed)

        return token
