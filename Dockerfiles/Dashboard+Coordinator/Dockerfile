FROM ubuntu:18.04

#installing pip and python
RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev 

#working directory
WORKDIR /app

COPY entryPoint.sh /app/

#copying required modules and files
COPY ./Dashboard /app/Dashboard

COPY ./Utilities /app/Utilities

COPY ./Coordinator /app/Coordinator

COPY .env /app/

#installing required modules
RUN pip3 install -r Dashboard/requirements.txt -r Coordinator/requirements.txt 

ENTRYPOINT ["/app/entryPoint.sh"]
