FROM buildpack-deps:latest

# runtime dependencies
RUN apt-get update && apt-get install -y \
  libarchive-dev \
  libgmp-dev  \
  libxft-dev \
  libxpm-dev

# retreive source code from github
RUN cd /usr/local/src \
  && git clone "https://github.com/swi-prolog/swipl.git" \
  && git clone "https://github.com/cliopatria/cliopatria"

# build swi-prolog core
RUN cd /usr/local/src/swipl \
  && ./prepare --yes \
  && ./configure \
  && make \
  && make install

# build swi-prolog packages
RUN cd /usr/local/src/swipl/packages \
  && ./configure
  && make \
  && make install

CMD ["swipl"]
