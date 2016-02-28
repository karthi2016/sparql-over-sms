from pipelines.actions import RunSparqlQuery
from pipelines.basepipeline import BasePipeline
from pipelines.filters import Base64Decode


class ReceiveSparqlQuery(BasePipeline):
    """Pipeline that handles incoming SPARQL queries"""

    chain = [
        Base64Decode,
        RunSparqlQuery
    ]
