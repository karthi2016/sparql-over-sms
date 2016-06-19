from SPARQLWrapper import SPARQLWrapper
from utilities.configuration import ConfigManager


class RunSparqlUpdate:
    """Runs a SPARQL update against a triple store"""
    name = "RunSparqlUpdate"
    description = "Runs a SPARQL update against a triple store"

    @staticmethod
    def execute(token):
        configmanager = ConfigManager()
        endpoint = configmanager.get_option("persistence", "triplestore", "query")

        # initialize sparql endpoint
        sparql = SPARQLWrapper(endpoint)

        # prepare sparql update
        sparql.setQuery(token.message.body)
        sparql.method = 'POST'
        sparql.returnFormat = 'json'

        # return result un-altered
        token.result = sparql.query().convert()


