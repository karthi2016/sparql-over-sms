package org.sparqloversms.algorithm.encoding;

import org.rdfhdt.hdt.dictionary.Dictionary;
import org.rdfhdt.hdt.enums.TripleComponentRole;
import org.rdfhdt.hdt.hdt.HDT;
import org.sparqloversms.algorithm.encoding.interfaces.Decoder;
import org.sparqloversms.algorithm.encoding.model.DecoderResult;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class HDTDecoder implements Decoder {

    private Dictionary dictionary;

    public HDTDecoder(HDT knowledge) {
        this.dictionary = knowledge.getDictionary();
    }

    /*-----------------------------------------------------------------------*/

    public DecoderResult decode(String input) {
        DecoderResult result = new DecoderResult();
        String temp = input;

        Pattern pat = Pattern.compile("\\$\\w{1,5}");
        Matcher m = pat.matcher(temp);

        Set<String> placeholders = new HashSet<>();
        while (m.find()) {
            placeholders.add(m.group());
        }

        for (String placeholder : placeholders) {
            String uri = getUriFromDictionary(placeholder);
            temp = temp.replaceAll(Pattern.quote(placeholder), String.format("<%s>", uri));
        }

        result.setOutput(temp);
        return result;
    }

    private String getUriFromDictionary(String placeholder) {
        String hexidecimal = placeholder.substring(1);
        int id = Integer.parseInt(hexidecimal, 16);

        return dictionary.idToString(id, TripleComponentRole.SUBJECT).toString();
    }
}
