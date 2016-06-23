package org.sparqloversms.algorithm.reasoning.interfaces;

import org.apache.jena.rdf.model.Model;

public interface Reasoner {

    Model removeRedundancy(Model input);

}
