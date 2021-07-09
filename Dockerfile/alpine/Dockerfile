#base image alpine
FROM alpine:3.10

WORKDIR /home/flask

COPY entryPoint.sh /home/flask/

RUN apk update \
    && apk add clamav clamav-daemon\
    && apk add clamav-libunrar\
    && mkdir /run/clamav/ && touch /run/clamav/clamd.pid && touch /run/clamav/clamd.sock\
    && chmod -R 777 /run/clamav\
    && chmod a+rwx /var/log/clamav/
 
RUN freshclam 

ENTRYPOINT [ "/home/flask/entryPoint.sh" ]

