package org.sparqloversms.compression.reasoning;

import org.apache.jena.rdf.model.*;
import org.apache.jena.vocabulary.OWL;
import org.apache.jena.vocabulary.RDF;
import org.apache.jena.vocabulary.RDFS;
import org.sparqloversms.compression.reasoning.interfaces.Reasoner;

import java.util.ArrayList;
import java.util.List;

public class RDFSReasoner implements Reasoner {

    private Model knowledge;

    public RDFSReasoner(Model knowledge) {
        this.knowledge = knowledge;
    }

    @Override
    public Model removeRedundancy(Model input) {
        List<Statement> redundant = new ArrayList<>();

        // Predefined selectors
        Selector typeTripleSelector = new SimpleSelector(null, RDF.type, null, "");
        Selector resourceTripleSelector = new SimpleSelector(null, RDF.type, RDFS.Resource);
        Selector subPropertyTripleSelector = new SimpleSelector(null, RDFS.subPropertyOf, null, "");
        Selector subClassOfResourceTripleSelector = new SimpleSelector(null, RDFS.subClassOf, RDFS.Resource);
        Selector subClassOfTripleSelector = new SimpleSelector(null, RDFS.subClassOf, null, "");
        Selector subPropertyOfMemberSelector = new SimpleSelector(null, RDFS.subPropertyOf, RDFS.member);
        Selector subClassOfLiteralSelector = new SimpleSelector(null, RDFS.subClassOf, RDFS.Literal);

        // Predefined triples
        List<Statement> allTriples = input.listStatements().toList();
        List<Statement> typeTriples = input.listStatements(typeTripleSelector).toList();
        List<Statement> resourceTriples = input.listStatements(resourceTripleSelector).toList();
        List<Statement> subPropertyTriples = input.listStatements(subPropertyTripleSelector).toList();
        List<Statement> subClassOfResourceTriples = input.listStatements(subClassOfResourceTripleSelector).toList();
        List<Statement> subClassOfTriples = input.listStatements(subClassOfTripleSelector).toList();
        List<Statement> subPropertyOfMemberTriples = input.listStatements(subPropertyOfMemberSelector).toList();
        List<Statement> subClassOfLiteralTriples = input.listStatements(subClassOfLiteralSelector).toList();

        // RDFS entailment pattern 2
        for (Statement typeTriple : typeTriples) {
            Selector subjectTripleSelector = new SimpleSelector(typeTriple.getSubject(), null, null, "");
            StmtIterator subjectTriples = input.listStatements(subjectTripleSelector);

            while (subjectTriples.hasNext()) {
                Statement triple = subjectTriples.next();
                Resource predicate = triple.getPredicate().asResource();
                Resource object = typeTriple.getObject().asResource();

                if (knowledge.contains(predicate, RDFS.domain, object)) {
                    redundant.add(typeTriple);
                    break;
                }
            }
        }

        // RDFS entailment pattern 3
        for (Statement typeTriple : typeTriples) {
            Selector subjectTripleSelector = new SimpleSelector(null, null, typeTriple.getSubject());
            StmtIterator subjectTriples = input.listStatements(subjectTripleSelector);

            while (subjectTriples.hasNext()) {
                Statement triple = subjectTriples.next();
                Resource predicate = triple.getPredicate().asResource();
                Resource object = typeTriple.getObject().asResource();

                if (knowledge.contains(predicate, RDFS.range, object)) {
                    redundant.add(typeTriple);
                    break;
                }
            }
        }

        // RDFS entailment pattern 4
        for (Statement resourceTriple : resourceTriples) {
            if (input.contains(null, null, resourceTriple.getSubject())) {
                redundant.add(resourceTriple);
                continue;
            }

            Selector selector = new SimpleSelector(resourceTriple.getSubject(), null, null, "");
            StmtIterator selection = input.listStatements(selector);
            while (selection.hasNext()) {
                Statement triple = selection.next();

                if (!triple.getPredicate().equals(resourceTriple.getPredicate())
                ||  !triple.getObject().equals(resourceTriple.getObject())) {
                    redundant.add(resourceTriple);
                    break;
                }
            }
        }

        // RDFS entailment pattern 5
        for (Statement subPropertyTriple : subPropertyTriples) {
            Resource subject = subPropertyTriple.getSubject();
            Resource object = subPropertyTriple.getObject().asResource();

            Selector subPropertyOfObjectTripleSelector = new SimpleSelector(null, RDFS.subPropertyOf, object);
            StmtIterator selection = input.listStatements(subPropertyOfObjectTripleSelector);
            while (selection.hasNext()) {
                Statement triple = selection.next();
                if (knowledge.contains(subject, RDFS.subPropertyOf, triple.getSubject())) {
                    redundant.add(subPropertyTriple);
                    break;
                }
            }
        }

        // RDFS entailment pattern 6
        for (Statement subPropertyTriple : subPropertyTriples) {
            Resource subject = subPropertyTriple.getSubject();
            Resource object = subPropertyTriple.getObject().asResource();

            if (subject.equals(object) && knowledge.contains(subject, RDF.type, RDF.Property)) {
                redundant.add(subPropertyTriple);
            }
        }

        // RDFS entailment pattern 7
        for (Statement triple : allTriples) {
            Selector subPropertyOfPredicateTripleSelector = new SimpleSelector(null, RDFS.subPropertyOf, triple.getPredicate());
            StmtIterator selection = input.listStatements(subPropertyOfPredicateTripleSelector);
            while (selection.hasNext()) {
                Statement subPropertyTriple = selection.next();

                Resource subject = triple.getSubject();
                Property predicate = ResourceFactory.createProperty(subPropertyTriple.getSubject().getURI());
                RDFNode object = triple.getObject();

                if (knowledge.contains(subject, predicate, object)) {
                    redundant.add(triple);
                    break;
                }
            }
        }

        // RDFS entailment pattern 8
        for (Statement subClassOfResourceTriple : subClassOfResourceTriples) {
            if (input.contains(subClassOfResourceTriple.getSubject(), RDF.type, RDFS.Class)) {
                redundant.add(subClassOfResourceTriple);
            }
        }

        // RDFS entailment pattern 9
        for (Statement typeTriple : typeTriples) {
            List<RDFNode> types = input.listObjectsOfProperty(typeTriple.getSubject(), RDF.type).toList();
            if (types.size() <= 1) {
                continue;
            }

            for (RDFNode type : types) {
                List<RDFNode> otherTypes = new ArrayList<>(types);
                otherTypes.remove(type);

                Resource typeSubject = type.asResource();
                for (RDFNode otherType : otherTypes) {
                    if (knowledge.contains(typeSubject, RDFS.subClassOf, otherType)) {
                        redundant.add(typeTriple);
                    }
                }
            }
        }

        // RDFS entailment pattern 10
        for (Statement subClassOfTriple : subClassOfTriples) {
            Resource subject = subClassOfTriple.getSubject();
            RDFNode object = subClassOfTriple.getObject();

            if (subject.equals(object) && knowledge.contains(subject, RDF.type, RDFS.Class)) {
                redundant.add(subClassOfTriple);
            }
        }

        // RDFS entailment pattern 11
        for (Statement subClassOfTriple : subClassOfTriples) {
            Selector subClassOfObjectTripleSelector = new SimpleSelector(null, RDFS.subClassOf, subClassOfTriple.getObject());
            StmtIterator selection = input.listStatements(subClassOfObjectTripleSelector);
            while (selection.hasNext()) {
                Statement subClassOfObjectTriple = selection.next();
                Resource subject = subClassOfTriple.getSubject();
                Resource object = subClassOfObjectTriple.getSubject();

                if (knowledge.contains(subject, RDFS.subClassOf, object)) {
                    redundant.add(subClassOfTriple);
                }
            }
        }

        // RDFS entailment pattern 12
        for (Statement subPropertyOfMemberTriple : subPropertyOfMemberTriples) {
            Resource subject = subPropertyOfMemberTriple.getSubject();

            if (knowledge.contains(subject, RDF.type, RDFS.ContainerMembershipProperty)) {
                redundant.add(subPropertyOfMemberTriple);
            }
        }

        // RDFS entailment pattern 13
        for (Statement subClassOfLiteralTriple : subClassOfLiteralTriples) {
            Resource subject = subClassOfLiteralTriple.getSubject();

            if (knowledge.contains(subject, RDF.type, RDFS.Datatype)) {
                redundant.add(subClassOfLiteralTriple);
            }
        }

        // OWL
        for (Statement triple : allTriples) {
            Resource subject = triple.getSubject();
            Property predicate = triple.getPredicate();
            RDFNode object = triple.getObject();

            if (!object.isURIResource()) {
                continue;
            }

            // SymmetricProperty
            Statement symmetricTriple = ResourceFactory.createStatement(object.asResource(), predicate, subject);
            if (input.contains(symmetricTriple)) {
                if (knowledge.contains(predicate, RDF.type, OWL.SymmetricProperty)) {
                    // Remove either (s, p, o) or (o, p, s)
                    if (!redundant.contains(triple) && !redundant.contains(symmetricTriple)) {
                        redundant.add(symmetricTriple);
                    }
                }
            }

            // InverseOf
            Selector inverseOfPredicate = new SimpleSelector(predicate, OWL.inverseOf, null, "");
            StmtIterator selection = knowledge.listStatements(inverseOfPredicate);
            while (selection.hasNext()) {
                Statement inverseOfTriple = selection.next();

                if (!inverseOfTriple.getObject().isURIResource()) {
                    continue;
                }

                Property inverseOfTripleObjectAsProperty = ResourceFactory.createProperty(inverseOfTriple.getObject().asResource().getURI());
                Statement inverseTriple = ResourceFactory.createStatement(object.asResource(), inverseOfTripleObjectAsProperty, subject);

                if (input.contains(object.asResource(), inverseOfTripleObjectAsProperty, subject)) {
                    // Remove either (s, p, o) or (o, o2, s)
                    if (!redundant.contains(triple) && !redundant.contains(inverseTriple)) {
                        redundant.add(inverseTriple);
                    }
                }
            }
        }

        return input.remove(redundant);
    }
}
