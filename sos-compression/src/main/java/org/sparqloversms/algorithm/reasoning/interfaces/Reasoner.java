package org.sparqloversms.algorithm.reasoning.interfaces;

import org.apache.jena.rdf.model.Model;
import org.sparqloversms.algorithm.reasoning.models.ReasonerResult;

public interface Reasoner {

    ReasonerResult removeRedundancy(Model input);

}
