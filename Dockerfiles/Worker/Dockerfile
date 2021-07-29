FROM ubuntu:18.04        

#Installing Python ClamAV
RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev \
    && apt-get install clamav clamav-daemon -y\
    && mkdir /run/clamav/ && touch /run/clamav/clamd.pid && touch /run/clamav/clamd.sock\
    && chmod -R 777 /run/clamav\
    && chmod a+rwx /var/log/clamav/ 

#Running Freshclam for downloading virus definations
RUN freshclam

#Working Directory
WORKDIR /app

#Copying Script which will run python files and ClamAV daemon
COPY entryPoint.sh /app/

#Copying Worker files to container working directory
COPY ./Worker /app/Worker

COPY ./Utilities /app/Utilities

COPY .env /app/

#Installing Modules
RUN pip3 install -r Worker/requirements.txt

#Starting the Script
ENTRYPOINT [ "/app/entryPoint.sh" ]