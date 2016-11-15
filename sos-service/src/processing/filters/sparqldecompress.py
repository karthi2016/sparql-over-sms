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

        # only if no errors occured
        if not decompressed_body.startswith('org.apache.jena'):
            token.message.body = ' '.join(decompressed_body.split())
