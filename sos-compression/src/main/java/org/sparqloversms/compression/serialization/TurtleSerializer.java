package org.sparqloversms.compression.serialization;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.util.FileUtils;
import org.sparqloversms.compression.serialization.interfaces.Serializer;

import java.io.IOException;
import java.io.StringWriter;

public class TurtleSerializer implements Serializer {

    public String serialize(String input) {
        return null;
    }

    @Override
    public String serialize(Model model) {
        String output = null;

        try(final StringWriter sw = new StringWriter())
        {
            model.write(sw, FileUtils.langTurtle);
            output = sw.toString();
        } catch (IOException e) {
            e.printStackTrace();
        }

        return output;
    }
}
