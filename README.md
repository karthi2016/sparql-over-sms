# SPARQL over SMS
Efficient transfer of SPARQL queries and results over short-message networks.

| master | develop |
|:------:|:-------:|
| [![Build Status](https://img.shields.io/travis/onnovalkering/sparql-over-sms/master.svg)](https://travis-ci.org/onnovalkering/sparql-over-sms) | [![Build Status](https://img.shields.io/travis/onnovalkering/sparql-over-sms/develop.svg)](https://travis-ci.org/onnovalkering/sparql-over-sms) |
| [![Coverage Status](https://img.shields.io/coveralls/onnovalkering/sparql-over-sms/master.svg)](https://coveralls.io/github/onnovalkering/sparql-over-sms) | [![Coverage Status](https://img.shields.io/coveralls/onnovalkering/sparql-over-sms/develop.svg)](https://coveralls.io/github/onnovalkering/sparql-over-sms) |


## Introduction
Many ICT applications and services, including those from the Semantic Web, rely on the Web for the exchange of data. Most rural areas of developing countries are not reached by the Web and its possibilities, while at the same time the ability to share knowledge has been identified as a key enabler for development. To make widespread knowledge sharing possible in these rural areas, the notion of the Web has to be downscaled based on the specific low-resource infrastructure in place. 

SPARQL over SMS is a solution for Web-like exchange of RDF data over low-bandwidth networks. This is made possible by a data compression method that combines generic compression strategies and strategies that use Semantic Web specific features to reduce the size of RDF before it is transferred over a low-bandwidth network. Although the SPARQL over SMS is based on ICT4D cases, it is also applicable to low-bandwidth cases in general, including the Internet of Things (IoT).

The paper that covers SPARQL over SMS:

Onno Valkering, Victor de Boer, Gossa Lô, Romy Blankendaal, and Stefan Schlobach. **The Semantic Web in an SMS**. _Proceedings of 20th International Conference on Knowledge Engineering and Knowledge Management (EKAW 2016)_

## Features
The features that are currently supported:

#### Networks:
WiFi (HTTP), Cellular (SMS)

#### SPARQL Query Forms:
CONSTRUCT, ASK

#### SPARQL Update Forms:
INSERT DATA, DELETE DATA

## Requirements
To be able to run SPARQL over SMS, at minimum, the following must be installed:

- Python 3.4+
- Java 1.8+
- Redis 3.2+

For the full set of features, a triple store is also required. Currently only [ClioPatria](https://github.com/ClioPatria/ClioPatria) is supported.
