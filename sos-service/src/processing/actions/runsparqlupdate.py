from SPARQLWrapper import SPARQLWrapper
from utilities import configmanager


class RunSparqlUpdate:
    """Runs a SPARQL-update against a triple store"""
    name = "RunSparqlUpdate"
    description = "Runs a SPARQL-update against a triple store"

    @staticmethod
    def execute(token):
        triplestore_host = configmanager.get_config("triplestore_host", 'localhost')
        endpoint = "http://{0}:3020/sparql/update".format(triplestore_host)

        # initialize sparql endpoint
        sparql = SPARQLWrapper(endpoint)

        # prepare sparql update
        sparql.setQuery(token.message.get_body())
        sparql.method = 'POST'
        sparql.returnFormat = 'rdf+xml'

        # return result un-altered
        result = sparql.query().convert()
        token.result = result.toxml()
