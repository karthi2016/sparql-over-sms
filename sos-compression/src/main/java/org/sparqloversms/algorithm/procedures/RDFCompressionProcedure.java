package org.sparqloversms.algorithm.procedures;

import org.apache.jena.rdf.model.Model;
import org.sparqloversms.algorithm.encoding.interfaces.Encoder;
import org.sparqloversms.algorithm.encoding.model.EncoderResult;
import org.sparqloversms.algorithm.procedures.interfaces.Procedure;
import org.sparqloversms.algorithm.procedures.models.ProcedureReport;
import org.sparqloversms.algorithm.reasoning.interfaces.Reasoner;
import org.sparqloversms.algorithm.reasoning.models.ReasonerResult;
import org.sparqloversms.algorithm.serialization.interfaces.Serializer;
import org.sparqloversms.algorithm.serialization.models.SerializerResult;

public class RDFCompressionProcedure implements Procedure {

    private Reasoner reasoner;
    private Serializer serializer;
    private Encoder encoder;

    public RDFCompressionProcedure(Reasoner reasoner, Serializer serializer, Encoder encoder) {
        this.reasoner = reasoner;
        this.serializer = serializer;
        this.encoder = encoder;
    }

    /*-----------------------------------------------------------------------*/

    @Override
    public ProcedureReport run(Model procedureInput) {
        ProcedureReport report = new ProcedureReport();

        // Step 1 - remove redundancy
        Model reasonerInput = procedureInput;
        ReasonerResult reasonerResult = reasoner.removeRedundancy(reasonerInput);
        report.setResult(reasonerResult);

        // Step 2 - serialize
        Model serializerInput = reasonerResult.getOutput();
        SerializerResult serializerResult = serializer.serialize(serializerInput);
        report.setResult(serializerResult);

        // Step 3 - encode
        String encoderInput = serializerResult.getOutput();
        EncoderResult encoderResult = encoder.encode(encoderInput);
        report.setResult(encoderResult);

        return report.finish();
    }
}

