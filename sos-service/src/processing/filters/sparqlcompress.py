from utilities.compression import SoSCompression


class SparqlCompress:
    """Performs SPARQL sos-compression"""
    name = "SparqlCompress"
    description = "Performs SPARQL sos-compression"

    @staticmethod
    def execute(token):
        message = token.message
        body = message.get_body()

        compressed_body = SoSCompression.compress_sparql(body)[0].decode('utf-8')

        # re-assign compressed body
        token.message.body = compressed_body
