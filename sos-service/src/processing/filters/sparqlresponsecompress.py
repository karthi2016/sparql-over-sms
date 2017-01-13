from utilities.compression import SoSCompression


class SparqlResponseCompress:
    """Performs SPARQL response sos-compression"""
    name = "SparqlCompress"
    description = "Performs RDF sos-compression"

    @staticmethod
    def execute(token):
        message = token.message
        body = message.get_body()

        print(body)

        compressed_body_parts = SoSCompression.compress_sparqlresponse(body)
        compressed_body = (b' '.join(compressed_body_parts)).decode('utf-8')

        # re-assign compressed body
        token.message.body = ' '.join(compressed_body.split())
