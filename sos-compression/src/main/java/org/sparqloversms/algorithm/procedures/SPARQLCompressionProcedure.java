package org.sparqloversms.algorithm.procedures;

import org.apache.jena.rdf.model.Model;
import org.sparqloversms.algorithm.encoding.interfaces.Encoder;
import org.sparqloversms.algorithm.encoding.model.EncoderResult;
import org.sparqloversms.algorithm.procedures.interfaces.Procedure;
import org.sparqloversms.algorithm.procedures.models.ProcedureReport;
import org.sparqloversms.algorithm.serialization.interfaces.Serializer;
import org.sparqloversms.algorithm.serialization.models.SerializerResult;

public class SPARQLCompressionProcedure implements Procedure {

    private Serializer serializer;
    private Encoder encoder;

    public SPARQLCompressionProcedure(Serializer serializer, Encoder encoder) {
        this.serializer = serializer;
        this.encoder = encoder;
    }

    /*-----------------------------------------------------------------------*/

    @Override
    public ProcedureReport run(Model procedureInput) {
        ProcedureReport report = new ProcedureReport();

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
