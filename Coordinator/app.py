from pymongo import MongoClient
import os
import sys
import clamd
from redis import Redis
from rq import Queue, Retry
from dotenv import load_dotenv

load_dotenv()

utilitiesPath = os.getenv("UTILITIES_PATH")

sys.path.insert(0, utilitiesPath)
from scanJob import scan,webcrawler

q = Queue(connection=Redis(host=os.getenv('REDIS_HOST'),port=int(os.getenv("REDIS_PORT"))))

uploadDirPath = os.getenv("UPLOAD_DIRECTORY")

mongodbHost = os.getenv("MONGODB_HOST")
mongodbPort = int(os.getenv("MONGODB_PORT"))

client = MongoClient(mongodbHost, mongodbPort)
scan8 = client['scan8']
links = scan8['links']
runninglinks = scan8['runninglinks']
prequeuedScans = scan8['prequeuedScans']
queuedScans = scan8['queuedScans']

if __name__ == '__main__':
    # Listen to changes in prequeuedScans collection
    while(True):
        prequeued = list(prequeuedScans.find())
        if(len(prequeued) > 0):
            id = prequeued[0]["_id"]
            dir = os.path.abspath(uploadDirPath) + "/" + id
            queuedScans.insert_one(prequeued[0])
            prequeuedScans.delete_one({"_id": id})
            for file in os.listdir(dir):
                # add to RQ
                q.enqueue(scan, dir + "/" + file, job_timeout=3, retry=Retry(max=2))
                
        link = list(links.find())
        if(len(link) > 0):
            id = link[0]["_id"]
            url = link[0]["link"]
            prox = link[0]["proxy"]
            proxy = {'http': prox, 'https': prox} if prox else None 
            q.enqueue(webcrawler, url, id, proxy, retry=Retry(max=2))
            links.delete_one({"_id": id})
            runninglinks.insert_one({"_id": id})

