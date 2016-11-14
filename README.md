# SPARQL over SMS
Efficient transfer of SPARQL queries and results over short-message networks.

| master | develop |
|:------:|:-------:|
| [![Build Status](https://img.shields.io/travis/onnovalkering/sparql-over-sms/master.svg)](https://travis-ci.org/onnovalkering/sparql-over-sms) | [![Build Status](https://img.shields.io/travis/onnovalkering/sparql-over-sms/develop.svg)](https://travis-ci.org/onnovalkering/sparql-over-sms) |
| [![Coverage Status](https://img.shields.io/coveralls/onnovalkering/sparql-over-sms/master.svg)](https://coveralls.io/github/onnovalkering/sparql-over-sms) | [![Coverage Status](https://img.shields.io/coveralls/onnovalkering/sparql-over-sms/develop.svg)](https://coveralls.io/github/onnovalkering/sparql-over-sms) |


## Introduction
SPARQL over SMS shows that data sharing according to Semantic Web practices is possible even in areas without a Web infrastructure.
The development of SPARQL over SMS is based on multiple ICT4D cases, but it is also applicable to low-bandwidth cases in general.
For example in the context of disaster management or the Internet of Things.

Although the costs per transferred byte are relatively high for SMS messages, still some benefits apply.
For instance, the infrastructure is already in place and has a global reach which even includes some rural areas of development countries.
Also, the required hardware to be able to send SMS messages is widespread available and is relatively affordable.

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
