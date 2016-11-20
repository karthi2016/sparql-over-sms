from utilities.compression import SoSCompression


class SparqlCompress:
    """Performs SPARQL sos-compression"""
    name = "SparqlCompress"
    description = "Performs SPARQL sos-compression"

    @staticmethod
    def execute(token):
        message = token.message
        body = message.get_body()

        compressed_body_parts = SoSCompression.decompress_sparql(body)
        compressed_body = (b' '.join(compressed_body_parts)).decode('utf-8')

        # only if no errors occured
        if not compressed_body.startswith('org.apache.jena'):
            token.message.body = ' '.join(compressed_body.split())
