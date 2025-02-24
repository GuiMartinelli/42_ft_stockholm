FROM alpine:latest

RUN apk update && apk add --no-cache python3 py3-pip py3-cryptography py3-pycryptodome

RUN adduser -D victim
WORKDIR /home/victim
COPY ./infra/infection ./infection
COPY ./stockholm.py ./
RUN chown -R victim:victim /home/victim

USER victim

CMD ["tail", "-f", "/dev/null"]