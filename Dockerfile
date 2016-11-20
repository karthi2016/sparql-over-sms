FROM debian:jessie
MAINTAINER onno.valkering@gmail.com

# install java and python
RUN apt-get update && apt-get install -y \
    openjdk-8-jdk \
    python3 \
    wget

# install maven
RUN wget http://apache.40b.nl/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz && \
    tar -zxf apache-maven-3.3.9-bin.tar.gz && \
    cp -R apache-maven-3.3.9 /usr/local && \
    ln -s /usr/local/apache-maven-3.3.9/bin/mvn /usr/bin/mvn

# install pip and virtualenv
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    pip3 install virtualenv

COPY . /
RUN ./sparqloversms.sh install

CMD ["docker"]
ENTRYPOINT ["./sparqloversms.sh"]

EXPOSE 8888