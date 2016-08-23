import rdflib

from SPARQLWrapper import SPARQLWrapper
from utilities.configuration import ConfigManager


class RunSparqlQuery:
    """Runs a SPARQL query against a triple store"""
    name = "RunSparqlQuery"
    description = "Runs a SPARQL query against a triple store"

    @staticmethod
    def execute(token):
        configmanager = ConfigManager()
        endpoint = configmanager.get_option("persistence", "triplestore", "query")

        # initialize sparql endpoint
        sparql = SPARQLWrapper(endpoint)

        # prepare sparql update
        sparql.setQuery(token.message.body)
        sparql.method = 'GET'
        sparql.returnFormat = 'rdf+xml'

        # return result un-altered
        result = sparql.query().convert()
        if type(result) is rdflib.ConjunctiveGraph:
            if len(result) <= 40:
                token.result = result.serialize(format='nt').decode('utf-8')
            else:
                token.result = result.serialize(format='turtle').decode('utf-8')
        else:
            token.result = result.toxml()


