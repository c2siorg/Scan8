#!/bin/bash

#checking if directory exists or not
if [ ! -d "/app/common/Results" ]
then 
    mkdir -p /app/common/Uploads
    mkdir -p /app/common/Results    
fi

#Running Flask Web Server

cd Dashboard
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
nohup python3 app.py &

cd ..

#Running Coordinator node

cd Coordinator
nohup python3 app.py &
cd ..

/bin/bash