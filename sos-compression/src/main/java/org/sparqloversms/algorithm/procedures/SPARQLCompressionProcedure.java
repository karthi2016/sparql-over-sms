package org.sparqloversms.algorithm.procedures;

import org.apache.commons.lang3.CharSet;
import org.apache.jena.rdf.model.InfModel;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdf.model.ModelFactory;
import org.apache.jena.rdf.model.Resource;
import org.apache.jena.riot.Lang;
import org.apache.jena.riot.RDFDataMgr;
import org.apache.jena.util.CharEncoding;
import org.apache.jena.util.FileUtils;
import org.apache.jena.vocabulary.RDF;
import org.sparqloversms.algorithm.encoding.interfaces.Encoder;
import org.sparqloversms.algorithm.encoding.model.EncoderResult;
import org.sparqloversms.algorithm.procedures.interfaces.Procedure;
import org.sparqloversms.algorithm.procedures.models.CompressionReport;
import org.sparqloversms.algorithm.serialization.interfaces.Serializer;
import org.sparqloversms.algorithm.serialization.models.SerializerResult;
import org.topbraid.spin.model.SPINFactory;
import org.topbraid.spin.vocabulary.SP;

import java.io.File;
import java.io.IOException;
import java.io.StringReader;
import java.nio.charset.Charset;

public class SPARQLCompressionProcedure implements Procedure {

    private Serializer serializer;
    private Encoder encoder;

    public SPARQLCompressionProcedure(Serializer serializer, Encoder encoder) {
        this.serializer = serializer;
        this.encoder = encoder;
    }

    /*-----------------------------------------------------------------------*/

    @Override
    public CompressionReport run(Model procedureInput) {
        CompressionReport report = new CompressionReport();

        // Step 1 - serialize
        Model serializerInput = procedureInput;
        SerializerResult serializerResult = serializer.serialize(serializerInput);
        report.setResult(serializerResult);

        // Step 2 - encode
        String encoderInput = serializerResult.getOutput();
        EncoderResult encoderResult = encoder.encode(encoderInput);
        report.setResult(encoderResult);

        return report.finish();
    }
}
