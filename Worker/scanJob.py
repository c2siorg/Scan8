from pymongo import MongoClient
import clamd
import os
from dotenv import load_dotenv
import json

load_dotenv()

resultsPath = os.getenv("RESULTS_PATH")
cd = clamd.ClamdUnixSocket()

mongodbHost = os.getenv("MONGODB_HOST")
mongodbPort = int(os.getenv("MONGODB_PORT"))

client = MongoClient(mongodbHost, mongodbPort)
scan8 = client['scan8']
queuedScans = scan8['queuedScans']
runningScans = scan8['runningScans']
completedScans = scan8['completedScans']

# RQ job
def scan(filePath):
    id = filePath.split("/")[-2]
    name = filePath.split("/")[-1]
    queued = list(queuedScans.find({"_id": id}))
    if(len(queued) != 0):
        runningScans.insert_one(queued[0])
        queuedScans.delete_one({"_id": id})
    result = cd.scan(filePath)
    filename = id+"_"+name+"_"+".json"
    filename = resultsPath+"/"+filename
    with open(filename, "a+") as file:
        json.dump(result, file, indent=4)
    
    runningScans.update_one({"_id": id}, {'$inc': {'files.completed': 1}})

    running = list(runningScans.find({"_id": id}))
    if(len(running) != 0 and running[0]['files']['total'] == running[0]['files']['completed']):
        completedScans.insert_one(running[0])
        runningScans.delete_one({"_id": id})

    
