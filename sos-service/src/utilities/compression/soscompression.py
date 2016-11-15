from tempfile import mkstemp
from os import fdopen
from utilities.interoperability import JarWrapper


class SoSCompression:
    """Wrapper around the SoS compression method"""

    @staticmethod
    def compress_sparql(input_body):
        outfd, outsock_path = mkstemp()
        with fdopen(outfd, 'bw') as temp_file:
            temp_file.write(bytes(input_body, 'utf-8'))

        # call .jar via java CLI
        jar_filepath = 'C:\\Repositories\\Projects\\sparql-over-sms\\sos-compression\\target\\sos-compression-0.5.jar'
        jar = JarWrapper(jar_filepath)

        knowledge_filepath = 'C:\\Repositories\\Projects\\sparql-over-sms\\sos-compression\\target\\combined20.hdt'
        result = jar.execute('--compress', '--type=SPARQL', '--input={0}'.format(outsock_path), '--knowledge={0}'.format(knowledge_filepath))

        return result

    @staticmethod
    def decompress_sparql(input_body):
        outfd, outsock_path = mkstemp()
        with fdopen(outfd, 'bw') as temp_file:
            temp_file.write(bytes(input_body, 'utf-8'))

        # call .jar via java CLI
        jar_filepath = 'C:\\Repositories\\Projects\\sparql-over-sms\\sos-compression\\target\\sos-compression-0.5.jar'
        jar = JarWrapper(jar_filepath)

        knowledge_filepath = 'C:\\Repositories\\Projects\\sparql-over-sms\\sos-compression\\target\\combined20.hdt'
        result = jar.execute('--decompress', '--type=SPARQL', '--input={0}'.format(outsock_path), '--knowledge={0}'.format(knowledge_filepath))

        return result

    @staticmethod
    def compress_sparqlresponse(input_body):
        outfd, outsock_path = mkstemp()
        with fdopen(outfd, 'bw') as temp_file:
            temp_file.write(bytes(input_body, 'utf-8'))

        # call .jar via java CLI
        jar_filepath = 'C:\\Repositories\\Projects\\sparql-over-sms\\sos-compression\\target\\sos-compression-0.5.jar'
        jar = JarWrapper(jar_filepath)

        knowledge_filepath = 'C:\\Repositories\\Projects\\sparql-over-sms\\sos-compression\\target\\combined20.hdt'
        result = jar.execute('--compress', '--type=RDF', '--input={0}'.format(outsock_path), '--knowledge={0}'.format(knowledge_filepath))

        return result

    @staticmethod
    def decompress_sparqlresponse(input_body):
        outfd, outsock_path = mkstemp()
        with fdopen(outfd, 'bw') as temp_file:
            temp_file.write(bytes(input_body, 'utf-8'))

        # call .jar via java CLI
        jar_filepath = 'C:\\Repositories\\Projects\\sparql-over-sms\\sos-compression\\target\\sos-compression-0.5.jar'
        jar = JarWrapper(jar_filepath)

        knowledge_filepath = 'C:\\Repositories\\Projects\\sparql-over-sms\\sos-compression\\target\\combined20.hdt'
        result = jar.execute('--decompress', '--type=RDF', '--input={0}'.format(outsock_path), '--knowledge={0}'.format(knowledge_filepath))

        return result
