FROM python:3.5
MAINTAINER onno.valkering@gmail.com

COPY . /
EXPOSE 8888

RUN pip install --upgrade pip && pip install virtualenv
RUN ./sparqloversms.sh install

CMD ["docker-start"]
ENTRYPOINT ["./sparqloversms.sh"]