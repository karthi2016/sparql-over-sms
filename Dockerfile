FROM python:3.5

COPY . /sparql-over-sms
COPY ./tools/docker/bootstrap/run-server.sh . 
COPY ./tools/docker/bootstrap/run-worker.sh .

RUN pip3 install -r /sparql-over-sms/sos-service/requirements.txt

ENV C_FORCE_ROOT "true"

CMD ["./run-server.sh"]

EXPOSE 8888
