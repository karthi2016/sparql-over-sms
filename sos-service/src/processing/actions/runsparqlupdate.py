from SPARQLWrapper import SPARQLWrapper
from utilities.configuration import ConfigManager


class RunSparqlUpdate:
    """Runs a SPARQL-update against a triple store"""
    name = "RunSparqlUpdate"
    description = "Runs a SPARQL-update against a triple store"

    @staticmethod
    def execute(token):
        endpoint = "http://localhost:3020/sparql/update"

        # initialize sparql endpoint
        sparql = SPARQLWrapper(endpoint)

        # prepare sparql update
        sparql.setQuery(token.message.body)
        sparql.method = 'POST'
        sparql.returnFormat = 'rdf+xml'

        # return result un-altered
        result = sparql.query().convert()
        token.result = result.toxml()
