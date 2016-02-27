from pipelines.actions import RunSparqlQuery
from pipelines.filters import Base64Decode


class ReceiveSparqlQuery:
    """Pipeline that handles incoming SPARQL queries"""
    chain = [
        Base64Decode,
        RunSparqlQuery
    ]

    def handle(self, message):
        current = message
        for link in self.chain:
            current = link.execute(current)

        # last is considered result
        return current
