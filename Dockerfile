FROM debian:latest

RUN apt-get -y update
RUN apt-get -y install python3 python3-pip

COPY . /sparql-over-sms

RUN pip3 install --upgrade pip
RUN pip3 install -r /sparql-over-sms/sos-service/requirements.txt

CMD ["python3", "/sparql-over-sms/sos-service/src/bootstrap.py"]

EXPOSE 8888
