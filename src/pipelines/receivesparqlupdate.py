from pipelines.filters import Base64Decode


class ReceiveSparqlUpdate:
    """Pipeline that handles incoming SPARQL updates"""
    chain = [
        Base64Decode
    ]

    def handle(self, message):
        current = message
        for link in self.chain:
            current = link.execute(current)

        # last is considered result
        return current