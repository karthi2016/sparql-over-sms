from pipelines.actions import RunSparqlUpdate
from pipelines.basepipeline import BasePipeline
from pipelines.filters import Base64Decode


class ReceiveSparqlUpdate(BasePipeline):
    """Pipeline that handles incoming SPARQL updates"""

    chain = [
        Base64Decode,
        RunSparqlUpdate
    ]
