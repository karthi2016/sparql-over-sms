from utilities.compression import SoSCompression


class SparqlResponseDecompress:
    """Performs SPARQL response sos-decompression"""
    name = "SparqlCompress"
    description = "Performs SPARQL response sos-decompression"

    @staticmethod
    def execute(token):
        message = token.message
        body = message.get_body()

        decompressed_body = SoSCompression.decompress_sparqlresponse(body)[0].decode('utf-8')

        # re-assign compressed body
        token.message.body = decompressed_body
