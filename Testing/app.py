import unittest
import os
import json
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

mongodbHost = os.getenv("MONGODB_HOST")
mongodbPort = int(os.getenv("MONGODB_PORT"))

client = MongoClient(mongodbHost, mongodbPort)
scan8 = client['scan8']
prequeuedScans = scan8['prequeuedScans']
queuedScans = scan8['queuedScans']
runningScans = scan8['runningScans']
completedScans = scan8['completedScans']

class Testing(unittest.TestCase):
    def testUploadsDirectoryPresent(self):
        self.assertTrue(os.path.isdir(os.getenv("UPLOAD_DIRECTORY")))

    def testResultsDirectoryPresent(self):
        self.assertTrue(os.path.isdir(os.getenv("RESULTS_PATH")))

    def testUploads(self):
        completed = list(completedScans.find())[0]
        id = completed['_id']
        numFiles = completed['files']['total']
        finalDir = os.path.abspath(os.getenv("UPLOAD_DIRECTORY")) + "/" + id
        self.assertEqual(len(os.listdir(finalDir)), numFiles)

    def testResults(self):
        completed = list(completedScans.find())[0]
        id = completed['_id']
        numFiles = completed['files']['total']
        finalDir = os.path.abspath(os.getenv("RESULTS_PATH"))
        results = [x for x in os.listdir(finalDir) if x.startswith(id)]
        self.assertEqual(len(results), numFiles)

    def testResultsJSON(self):
        for filename in os.listdir(os.path.abspath(os.getenv("RESULTS_PATH"))):
            filepath = os.path.join(os.getenv("RESULTS_PATH"), filename)
            validJSON = True
            try:
                with open(filepath, 'r') as f:
                    jsonDict = json.load(f)
            except Exception as e:
                validJSON = False
        self.assertTrue(validJSON)


if __name__ == '__main__':
    unittest.main()
