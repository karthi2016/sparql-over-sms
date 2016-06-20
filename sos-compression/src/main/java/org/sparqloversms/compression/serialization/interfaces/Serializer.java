package org.sparqloversms.compression.serialization.interfaces;

public interface Serializer {
    String serialize(String input);

    String deserialize(String input);
}
