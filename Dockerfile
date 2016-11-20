FROM bash:4.4
MAINTAINER onno.valkering@gmail.com

# install java and python
RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
    apk update && apk add -f \
    openjdk8 \
    python3 \
    python3-dev \
    wget \
    dos2unix@testing

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
RUN chmod u+x sparqloversms.sh && \
    dos2unix sparqloversms.sh && \
    bash sparqloversms.sh install

ENTRYPOINT ["bash", "sparqloversms.sh"]
CMD ["docker"]

EXPOSE 8888