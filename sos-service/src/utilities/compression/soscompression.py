from tempfile import mkstemp
from os import fdopen
from utilities.interoperability import JarWrapper


class SoSCompression:
    """Wrapper around the SoS compression method"""
    jar_filepath = '..\\..\\sos-compression\\target\\sos-compression-1.0.jar'
    knowledge_filepath = '..\\..\\sos-compression\\src\\main\\resources\\knowledge\\combined20.hdt'

    @staticmethod
    def compress_sparql(input_body):
        outfd, outsock_path = mkstemp()
        with fdopen(outfd, 'bw') as temp_file:
            temp_file.write(bytes(input_body, 'utf-8'))

        # call .jar via java CLI
        jar = JarWrapper(SoSCompression.jar_filepath)

        result = jar.execute('--compress',
                             '--type=SPARQL',
                             '--input={0}'.format(outsock_path),
                             '--knowledge={0}'.format(SoSCompression.knowledge_filepath))

        return result

    @staticmethod
    def decompress_sparql(input_body):
        outfd, outsock_path = mkstemp()
        with fdopen(outfd, 'bw') as temp_file:
            temp_file.write(bytes(input_body, 'utf-8'))

        # call .jar via java CLI
        jar = JarWrapper(SoSCompression.jar_filepath)

        result = jar.execute('--decompress',
                             '--type=SPARQL',
                             '--input={0}'.format(outsock_path),
                             '--knowledge={0}'.format(SoSCompression.knowledge_filepath))

        return result

    @staticmethod
    def compress_sparqlresponse(input_body):
        outfd, outsock_path = mkstemp()
        with fdopen(outfd, 'bw') as temp_file:
            temp_file.write(bytes(input_body, 'utf-8'))

        # call .jar via java CLI
        jar = JarWrapper(SoSCompression.jar_filepath)

        result = jar.execute('--compress',
                             '--type=RDF',
                             '--input={0}'.format(outsock_path),
                             '--knowledge={0}'.format(SoSCompression.knowledge_filepath))

        return result

    @staticmethod
    def decompress_sparqlresponse(input_body):
        outfd, outsock_path = mkstemp()
        with fdopen(outfd, 'bw') as temp_file:
            temp_file.write(bytes(input_body, 'utf-8'))

        # call .jar via java CLI
        jar = JarWrapper(SoSCompression.jar_filepath)

        result = jar.execute('--decompress',
                             '--type=RDF',
                             '--input={0}'.format(outsock_path),
                             '--knowledge={0}'.format(SoSCompression.knowledge_filepath))

        return result
