from SPARQLWrapper import SPARQLWrapper
from services import ConfigManager, ServiceBox


class RunSparqlQuery:
    """Runs a SPARQL query against a triple store"""
    name = "RunSparqlQuery"
    description = "Runs a SPARQL query against a triple store"

    @staticmethod
    def execute(token):
        configmanager = ServiceBox.get_instance(ConfigManager)
        endpoint = configmanager.get_option("persistence", "triplestore", "query")

        # initialize sparql endpoint
        sparql = SPARQLWrapper(endpoint)

        # prepare sparql update
        sparql.setQuery(token.message.body)
        sparql.method = 'GET'
        sparql.returnFormat = 'json'

        # return result un-altered
        token.result = sparql.query().convert()


