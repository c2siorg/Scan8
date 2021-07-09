from pymongo import MongoClient
import os
import sys
import clamd
from redis import Redis
from rq import Queue
from dotenv import load_dotenv

load_dotenv()

workerPath = os.getenv("WORKER_PATH")

sys.path.insert(0, workerPath)
from scanJob import scan

q = Queue(connection=Redis())

uploadDirPath = os.getenv("UPLOAD_DIRECTORY")

mongodbHost = os.getenv("MONGODB_HOST")
mongodbPort = int(os.getenv("MONGODB_PORT"))

client = MongoClient(mongodbHost, mongodbPort)
scan8 = client['scan8']
prequeuedScans = scan8['prequeuedScans']
queuedScans = scan8['queuedScans']

if __name__ == '__main__':
    # Listen to changes in prequeuedScans collection
    while(True):
        prequeued = list(prequeuedScans.find())
        if(len(prequeued) > 0):
            id = prequeued[0]["_id"]
            dir = os.path.abspath(uploadDirPath) + "/" + id

            for file in os.listdir(dir):
                # add to RQ
                q.enqueue(scan, dir + "/" + file)
                
            queuedScans.insert_one(prequeued[0])
            prequeuedScans.delete_one({"_id": id})
