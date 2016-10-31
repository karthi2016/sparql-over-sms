docker run -P -d --hostname sos-rabbitmq --name sos-rabbitmq rabbitmq:management
docker run -P -d --link sos-rabbitmq:sos-rabbitmq sos-service
