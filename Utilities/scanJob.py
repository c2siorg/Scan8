from Webcrawler import WebCrawler
from pymongo import MongoClient
from redis import Redis
import clamd
import os
import json
from dotenv import load_dotenv
from hurry.filesize import size, si
from datetime import datetime
import shutil

load_dotenv()
upload_path = os.getenv("UPLOAD_DIRECTORY")
resultsPath = os.getenv("RESULTS_PATH")
cd = clamd.ClamdUnixSocket()

mongodbHost = os.getenv("MONGODB_HOST")
mongodbPort = int(os.getenv("MONGODB_PORT"))

client = MongoClient(mongodbHost, mongodbPort)
scan8 = client['scan8']
runninglinks = scan8['runninglinks']
prequeuedScans = scan8['prequeuedScans']
queuedScans = scan8['queuedScans']
runningScans = scan8['runningScans']
completedScans = scan8['completedScans']

redis_client = Redis(host=os.getenv('REDIS_HOST'),port=int(os.getenv("REDIS_PORT")))

def webcrawler(url,folder,proxy):
	try:
		crawler = WebCrawler()
		urls = crawler.get_urls(url,proxy)
		urls.add(url)
		for url in urls:
		    print(url)
		    crawler.download_file(url, upload_path + "/"+ folder, proxy)
		curTime = datetime.now()
		dirSize = 0
		numFiles = 0
		for element in os.scandir(upload_path + "/"+ folder):
			dirSize+=os.path.getsize(element)
			numFiles += 1
		runninglinks.delete_one({"_id": folder})	
		scan8.prequeuedScans.insert_one(
		    {"_id": str(folder), "submitTime": {"date": curTime.strftime("%d-%m-%Y"), "time": curTime.strftime(
		        "%H:%M:%S")}, "size": size(dirSize, system=si), "files": {"total": numFiles, "completed": 0}, "result": {"Virus": 0, "Virus_name": []}}
		)
	except:
		print("Taking too long to download files")
		runninglinks.delete_one({"_id": folder})	


# RQ job
def scan(filePath):
    id = filePath.split("/")[-2]
    name = filePath.split("/")[-1]
    queued = list(queuedScans.find({"_id": id}))
    if(len(queued) != 0):
        runningScans.insert_one(queued[0])
        queuedScans.delete_one({"_id": id})
        _queued = list(queuedScans.find())
        _running = list(runningScans.find({"_id": id}))
        redis_client.publish('scan_progress', json.dumps({ 'queued' : _queued, 'running': _running }))
    
    result = cd.scan(filePath)
    result = (result[(list(result.keys())[0])])
    if result[0] == "FOUND":
    	data = list(runningScans.find({"_id": id}))
    	runningScans.update_one({"_id": id}, {"$set": {'result.Virus': (((data[0])['result'])['Virus']) + 1}})
    	result_list=(((data[0])['result'])['Virus_name'])
    	result_list.append(result[1])
    	runningScans.update_one({"_id": id}, {"$set": {'result.Virus_name': result_list }})
    	
    filename = id+"_"+name+"_"+".json"
    filename = resultsPath+"/"+filename
    with open(filename, "a+") as file:
        json.dump(result, file, indent=4)
    
    runningScans.update_one({"_id": id}, {'$inc': {'files.completed': 1}})
    _running = list(runningScans.find())
    redis_client.publish('scan_progress', json.dumps({ 'running': _running }))

    running = list(runningScans.find({"_id": id}))
    if(len(running) != 0 and running[0]['files']['total'] == running[0]['files']['completed']):
        completedScans.insert_one(running[0])
        runningScans.delete_one({"_id": id})
        shutil.rmtree(upload_path + "/" + id)

        _running = list(runningScans.find())
        _completed = list(completedScans.find({"_id": id}))
        redis_client.publish('scan_progress', json.dumps({ 'completed' : _completed, 'running': _running }))
