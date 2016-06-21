package org.sparqloversms.compression.reasoning.interfaces;

import org.apache.jena.rdf.model.Model;

public interface Reasoner {

    Model removeRedundancy(Model input);

}
