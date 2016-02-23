from base64 import b64encode, b64decode


class SparqlProcessor:
    """Processes SPARQL queries"""

    def __init__(self, compressionconfig):
        self.compressionconfig = compressionconfig

    def pack(self, sparql):
        packed = b64encode(str.encode(sparql)).decode('utf-8')
        return packed

    def unpack(self, packed):
        sparql = b64decode(str.encode(packed)).decode('utf-8')
        return sparql
