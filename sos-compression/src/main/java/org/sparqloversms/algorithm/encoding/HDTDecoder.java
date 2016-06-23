package org.sparqloversms.algorithm.encoding;

import org.rdfhdt.hdt.dictionary.Dictionary;
import org.rdfhdt.hdt.enums.TripleComponentRole;
import org.sparqloversms.algorithm.encoding.interfaces.Decoder;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class HDTDecoder implements Decoder {

    private Dictionary dictionary;

    public HDTDecoder(Dictionary dictionary) {
        this.dictionary = dictionary;
    }

    /*-----------------------------------------------------------------------*/

    public String decode(String input) {
        Pattern pat = Pattern.compile("\\$\\w{1,5}");
        Matcher m = pat.matcher(input);

        List<String> placeholders = new ArrayList<>();
        while (m.find()) {
            placeholders.add(m.group());
        }

        for (String placeholder : placeholders) {
            String uri = getUriFromDictionary(placeholder);
            input = input.replaceAll(placeholder, String.format("<%s>", uri));
        }

        return input;
    }

    private String getUriFromDictionary(String placeholder) {
        String hexidecimal = placeholder.substring(1);
        int id = Integer.parseInt(hexidecimal, 16);

        return dictionary.idToString(id, TripleComponentRole.SUBJECT).toString();
    }
}
