from pipelines.basepipeline import BasePipeline
from pipelines.filters import Base64Encode
from pipelines.actions import SendSms


class SendSparqlUpdate(BasePipeline):
    """Pipeline that handles outgoing SPARQL updates"""

    chain = [
        Base64Encode,
        SendSms
    ]