package org.sparqloversms.algorithm.serialization.interfaces;

import org.apache.jena.rdf.model.Model;

public interface Serializer {
    String serialize(String input);

    String serialize(Model model);
}
