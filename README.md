# SPARQL over SMS
Efficient transfer of SPARQL queries and results over short-message networks.

### Introduction
SPARQL over SMS shows that data sharing according to Semantic Web practices is possible even in areas without a Web infrastructure. 
The development of SPARQL over SMS is based on multiple ICT4D cases, but it is also applicable to low-bandwidth cases in general.
For example in the context of disaster management or the Internet of Things.

Although the costs per transferred byte are relatively high for SMS messages, still some benefits apply. 
For instance, the infrastructure is already in place and has a global reach which even includes some rural areas of development countries. 
Also, the required hardware to be able to send SMS messages is widespread available and is relatively affordable.

### Getting started
To get SPARQL over SMS running within 5 minutes, run these commands on either Windows or Linux:

```shell
git clone https://github.com/onnovalkering/sparl-over-sms
cd sparql-over-sms

pip3 install -r requirements.txt
python3 src/bootstrap.py
```

For further customization, please consult the [documentation](https://github.com/onnovalkering/sparql-over-sms/wiki).

### Transfer rate
The developed conversion module can translate SPARQL over HTTP requests to SMS messages and decodes these messages at the other end.
The estimated number of triples that can be send per SMS are:

| SMSes | Triples |
| ----- | -----:|
| 2 | 3 |
| 4 | 9 |
| 6 | 66 |
| 8 | 116 |
| 10 | 301 |

### Requirements
For the use of SPARQL over SMS, the following are assumed to be installed:

- Python 3.4.2+