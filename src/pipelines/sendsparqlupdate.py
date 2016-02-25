from pipelines.filters import Base64Encode
from pipelines.actions import SendSms


class SendSparqlUpdate:
    """Pipeline that handles outgoing SPARQL updates"""
    chain = [
        Base64Encode,
        SendSms
    ]

    def handle(self, message):
        current = message
        for link in self.chain:
            current = link.execute(current)

        # last is considered result
        return current