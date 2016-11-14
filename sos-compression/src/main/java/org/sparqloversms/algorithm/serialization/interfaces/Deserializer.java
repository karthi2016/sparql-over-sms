package org.sparqloversms.algorithm.serialization.interfaces;

import org.sparqloversms.algorithm.serialization.models.DeserializerResult;

public interface Deserializer {

    DeserializerResult deserialize(String input);

}
