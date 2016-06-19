package org.sparqloversms.compression.encoding.interfaces;

public interface Encoder {
    String encode(String input);

    String decode(String input);
}
