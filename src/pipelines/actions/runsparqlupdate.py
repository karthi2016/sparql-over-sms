from SPARQLWrapper import SPARQLWrapper


class RunSparqlUpdate:
    """Runs a SPARQL update against a triple store"""

    @staticmethod
    def execute(message):
        from webapi import app
        sparql = SPARQLWrapper(app.config['c_triplestore']['endpoints']['update'])

        # prepare sparql update
        sparql.setQuery(message.body)
        sparql.method = 'POST'
        sparql.returnFormat = 'json'

        # return result un-altered
        return sparql.query().convert()


