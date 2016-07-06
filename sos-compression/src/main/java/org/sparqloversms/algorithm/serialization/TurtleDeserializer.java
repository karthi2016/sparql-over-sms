package org.sparqloversms.algorithm.serialization;

import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.util.FileUtils;
import org.sparqloversms.algorithm.serialization.interfaces.Deserializer;
import org.sparqloversms.algorithm.serialization.models.DeserializerResult;

import java.io.StringReader;

public class TurtleDeserializer implements Deserializer {

    @Override
    public DeserializerResult deserialize(String input) {
        DeserializerResult result = new DeserializerResult();

        Model model = ModelFactory.createDefaultModel();

        StringReader sr = null;
        try {
            sr = new StringReader(input);
            model.read(sr, null, FileUtils.langTurtle);
            result.setOutput(model);
        } catch (Exception e) {
            e.printStackTrace();
        }
        finally {
            if (sr != null) {
                sr.close();
            }
        }

        return result;
    }

}
