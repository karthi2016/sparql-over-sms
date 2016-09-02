# SPARQL over SMS
Efficient transfer of SPARQL queries and results over short-message networks.

|         | master | develop |
|---------|:------:|:-------:|
| Linux build  | [![Build Status](https://img.shields.io/travis/onnovalkering/sparql-over-sms/master.svg)](https://travis-ci.org/onnovalkering/sparql-over-sms) | [![Build Status](https://img.shields.io/travis/onnovalkering/sparql-over-sms/develop.svg)](https://travis-ci.org/onnovalkering/sparql-over-sms) |
| Windows build | [![Build Status](https://img.shields.io/appveyor/ci/onnovalkering/sparql-over-sms/master.svg)](https://ci.appveyor.com/project/onnovalkering/sparql-over-sms) | [![Build Status](https://img.shields.io/appveyor/ci/onnovalkering/sparql-over-sms/develop.svg)](https://ci.appveyor.com/project/onnovalkering/sparql-over-sms) |
| Coverage | [![Coverage Status](https://img.shields.io/coveralls/onnovalkering/sparql-over-sms/master.svg)](https://coveralls.io/github/onnovalkering/sparql-over-sms) | [![Coverage Status](https://img.shields.io/coveralls/onnovalkering/sparql-over-sms/develop.svg)](https://coveralls.io/github/onnovalkering/sparql-over-sms) |


### Introduction
SPARQL over SMS shows that data sharing according to Semantic Web practices is possible even in areas without a Web infrastructure.
The development of SPARQL over SMS is based on multiple ICT4D cases, but it is also applicable to low-bandwidth cases in general.
For example in the context of disaster management or the Internet of Things.

Although the costs per transferred byte are relatively high for SMS messages, still some benefits apply.
For instance, the infrastructure is already in place and has a global reach which even includes some rural areas of development countries.
Also, the required hardware to be able to send SMS messages is widespread available and is relatively affordable.

### Transfer rate
The developed conversion module can translate SPARQL over HTTP requests to SMS messages and decodes these messages at the other end.
The estimated number of triples that can be send per SMS are:

| SMSes | Triples |
| ----- | -----:|
| 2 | 3 |
| 4 | 16 |
| 6 | 84 |
| 8 | 126 |
| 10 | 301 |

### Requirements
For the use of SPARQL over SMS, the following must be installed:

- Python 3.4.2+
- RabbitMQ 3.6.0+
