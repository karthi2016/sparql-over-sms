from utilities.compression import SoSCompression


class SparqlDecompress:
    """Performs SPARQL sos-decompression"""
    name = "SparqlCompress"
    description = "Performs SPARQL sos-decompression"

    @staticmethod
    def execute(token):
        message = token.message
        body = message.get_body()

        decompressed_body_parts = SoSCompression.decompress_sparql(body)
        decompressed_body = (b' '.join(decompressed_body_parts)).decode('utf-8')

        # re-assign compressed body
        token.message.body = ' '.join(decompressed_body.split())
