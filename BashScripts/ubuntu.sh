#!/bin/bash
results=()
results2=()
wget --post-data "query=get_recent&selector=100" https://mb-api.abuse.ch/api/v1/
for i in {0..99}
do
    results+=($(jq ".data[$i].sha256_hash" index.html))
done
for i in "${results[@]}"
do
    results2+=($(sed -e 's/^"//' -e 's/"$//' <<<"$i")) 
done
mkdir /home/flask/toscan
for i in "${results2[@]}"
do
    wget -P /home/flask/toscan --post-data "query=get_file&sha256_hash=$i" https://mb-api.abuse.ch/api/v1/
done
mkdir /home/flask/realviruses
for i in /home/flask/toscan/*;
do 
    7z x -p"infected" $i -o/home/flask/realviruses
done
clamdscan /home/flask/realviruses

