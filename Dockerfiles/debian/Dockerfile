#base image ubuntu
FROM debian:jessie

WORKDIR /home/flask

COPY entryPoint.sh /home/flask/

RUN apt-get update -y \
    && apt-get install clamav clamav-daemon -y\
    && mkdir /run/clamav/ && touch /run/clamav/clamd.pid && touch /run/clamav/clamd.sock\
    && chmod -R 777 /run/clamav\
    && chmod a+rwx /var/log/clamav/ 
    
RUN freshclam 

ENTRYPOINT [ "/home/flask/entryPoint.sh" ]

