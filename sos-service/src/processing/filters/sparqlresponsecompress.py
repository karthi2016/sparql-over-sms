from utilities.compression import SoSCompression


class SparqlResponseCompress:
    """Performs SPARQL response sos-compression"""
    name = "SparqlCompress"
    description = "Performs RDF sos-compression"

    @staticmethod
    def execute(token):
        message = token.message
        body = message.get_body()

        compressed_body = SoSCompression.compress_sparqlresponse(body)[0].decode('utf-8')

        # re-assign compressed body
        token.message.body = compressed_body
