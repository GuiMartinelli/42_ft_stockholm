FROM debian:buster

RUN apt-get update

CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"