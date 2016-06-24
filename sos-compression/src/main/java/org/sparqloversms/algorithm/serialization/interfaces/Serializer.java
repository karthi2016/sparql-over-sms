package org.sparqloversms.algorithm.serialization.interfaces;

import org.apache.jena.rdf.model.Model;
import org.sparqloversms.algorithm.serialization.models.SerializerResult;

public interface Serializer {

    SerializerResult serialize(Model model);

}
