FROM ubuntu:18.04        

#Installing Python ClamAV
RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev \
    && apt-get install clamav clamav-daemon -y\
    && mkdir /run/clamav/ && touch /run/clamav/clamd.pid && touch /run/clamav/clamd.sock\
    && chmod -R 777 /run/clamav\
    && chmod a+rwx /var/log/clamav/ 

#running freshclam for downloading virus definations
RUN freshclam

#working Directory
WORKDIR /app

#copying script which will run python files and clamAV daemon
COPY entryPoint.sh /app/

#copying required modules and files into the container
COPY ./Worker /app/Worker

COPY ./Utilities /app/Utilities

COPY .env /app/

#installing Modules
RUN pip3 install -r Worker/requirements.txt


ENTRYPOINT [ "/app/entryPoint.sh" ]