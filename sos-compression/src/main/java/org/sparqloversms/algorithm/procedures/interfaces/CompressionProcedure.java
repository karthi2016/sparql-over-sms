package org.sparqloversms.algorithm.procedures.interfaces;

import org.apache.jena.rdf.model.Model;
import org.sparqloversms.algorithm.procedures.models.CompressionReport;

public interface CompressionProcedure {

    CompressionReport run(Model procedureInput);

}
