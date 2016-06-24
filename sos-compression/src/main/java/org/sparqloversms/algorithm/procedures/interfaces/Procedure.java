package org.sparqloversms.algorithm.procedures.interfaces;

import org.apache.jena.rdf.model.Model;
import org.sparqloversms.algorithm.procedures.models.ProcedureReport;

public interface Procedure {

    ProcedureReport run(Model procedureInput);

}
