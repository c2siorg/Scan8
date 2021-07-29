FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev 

WORKDIR /app

COPY entryPoint.sh /app/

COPY ./Dashboard /app/Dashboard

COPY ./Utilities /app/Utilities

COPY ./Coordinator /app/Coordinator

COPY .env /app/

RUN pip3 install -r Dashboard/requirements.txt -r Coordinator/requirements.txt 

ENTRYPOINT ["/app/entryPoint.sh"]
