package org.sparqloversms.compression.encoding;

import org.rdfhdt.hdt.dictionary.Dictionary;
import org.rdfhdt.hdt.enums.TripleComponentRole;
import org.rdfhdt.hdt.hdt.HDT;
import org.rdfhdt.hdt.hdt.HDTManager;
import org.sparqloversms.compression.encoding.interfaces.Encoder;
import java.io.IOException;

public class HDTEncoder implements Encoder {

    private HDT hdt;
    private Dictionary dictionary;

    public HDTEncoder(String hdtFileName) throws IOException {
        hdt = HDTManager.loadHDT(hdtFileName, null);
        dictionary = hdt.getDictionary();
    }

    /*-----------------------------------------------------------------------*/

    public String encode(String input) {
        try {
            String result = String.format("%d", dictionary.stringToId(input, TripleComponentRole.SUBJECT));
            return result;
        } catch (Exception ex) {
            return "-1";
        }
    }

    public String decode(String input) {
        try {
            String result = dictionary.idToString(Integer.parseInt(input), TripleComponentRole.SUBJECT).toString();
            return result;
        } catch (Exception ex) {
            return "-1";
        }
    }
}
