from pipelines.basepipeline import BasePipeline
from pipelines.filters import Base64Encode
from pipelines.actions import SendSms


class SendSparqlQuery(BasePipeline):
    """Pipeline that handles outgoing SPARQL queries"""

    chain = [
        Base64Encode,
        SendSms
    ]
