from rdflib import ConjunctiveGraph
from SPARQLWrapper import SPARQLWrapper
from utilities import configmanager


class RunSparqlQuery:
    """Runs a SPARQL-query against a triple store"""
    name = "RunSparqlQuery"
    description = "Runs a SPARQL-query against a triple store"

    @staticmethod
    def execute(token):
        triplestore_host = configmanager.get_config("triplestore_host")
        if triplestore_host is None:
            raise Exception("the 'triplestore_host' configuration is not set.")

        endpoint = "http://{0}:3020/sparql/".format(triplestore_host)

        # initialize sparql endpoint
        sparql = SPARQLWrapper(endpoint)

        print('query:')
        print(token.message.get_body())

        # prepare sparql update
        sparql.setQuery(token.message.get_body())
        sparql.method = 'POST'
        sparql.returnFormat = 'rdf+xml'

        # return result un-altered
        result = sparql.query().convert()
        if type(result) is ConjunctiveGraph:
            token.result = result.serialize().decode('utf-8')
        else:
            token.result = result.toxml()


