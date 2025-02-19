FROM alpine:latest

RUN apk update && apk add --no-cache python3 py3-pip py3-cryptography

RUN adduser -D victim
USER victim
WORKDIR /home/victim

COPY ./infra/infection ./infection
COPY ./stockholm.py ./

CMD ["tail", "-f", "/dev/null"]