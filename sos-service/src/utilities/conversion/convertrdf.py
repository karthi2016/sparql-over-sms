from rdflib import Graph


def convertrdf_bymimetype(rdf, mimetype):
    graph = Graph().parse(data=rdf, format='turtle')

    mimetype_mapping = {
        'text/turtle': 'turtle',
        'application/rdf+xml': 'xml',
        'application/ld+json': 'json-ld',
        'application/n-triples': 'nt',
        'text/n3': 'n3'
    }

    if ',' in mimetype:
        mimetype = mimetype[:mimetype.index(',')]

    rdf_format = mimetype_mapping.get(mimetype)
    converted = graph.serialize(format=rdf_format)

    return converted


