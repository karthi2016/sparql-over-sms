#!/bin/bash

DAEMON_DIR=./sos-service/src
DAEMON=$DAEMON_DIR/run-server.py
NAME=sparqloversms
DESC="SPARQL over SMS daemon"

test -f $DAEMON || exit 0

set -e

case "$1" in
  start)
        echo -n "Starting $DESC: "
        start-stop-daemon --start --pidfile /var/run/$NAME.pid \
            --chdir $DAEMON_DIR \
            --make-pidfile --background -c nobody --startas $DAEMON
        echo "$NAME."
        ;;
  stop)
        echo -n "Stopping $DESC: "
        start-stop-daemon --stop --quiet --oknodo \
            --pidfile /var/run/$NAME.pid
        rm -f /var/run/$NAME.pid
        echo "$NAME."
        ;;
  restart)
        echo -n "Restarting $DESC: "
        start-stop-daemon --stop --quiet --oknodo \
            --pidfile /var/run/$NAME.pid
        rm -f /var/run/$NAME.pid
        start-stop-daemon --start --pidfile /var/run/$NAME.pid \
            --chdir $DAEMON_DIR \
            --make-pidfile --background -c nobody --startas $DAEMON
        echo "$NAME."
esac

exit 0