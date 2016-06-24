package org.sparqloversms.algorithm.serialization;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.util.FileUtils;
import org.sparqloversms.algorithm.serialization.interfaces.Serializer;
import org.sparqloversms.algorithm.serialization.models.SerializerResult;

import java.io.IOException;
import java.io.StringWriter;

public class TurtleSerializer implements Serializer {

    @Override
    public SerializerResult serialize(Model model) {
        SerializerResult result = new SerializerResult();

        try(final StringWriter sw = new StringWriter())
        {
            model.write(sw, FileUtils.langTurtle);
            result.setOutput(sw.toString());
        } catch (IOException e) {
            e.printStackTrace();
        }

        return result;
    }
}
