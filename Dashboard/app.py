from flask import Flask, render_template, url_for, Response
import time
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient('localhost', 27017)
scan8 = client['scan8']
prequeuedScans = scan8['prequeuedScans']
queuedScans = scan8['queuedScans']
runningScans = scan8['runningScans']
completedScans = scan8['completedScans']

# TODO: add a caching layer to all routes


def index():
    prequeued = prequeuedScans.find()
    queued = queuedScans.find()
    running = runningScans.find()
    completed = completedScans.find()
    return render_template('index.html', prequeued=prequeued, queued=queued, running=running, completed=completed, newScanUrl=url_for('newScan'))


def new_scan():
    return render_template('newScan.html')


def progress():
    def generate():
        while True:
            running = runningScans.find()
            x = {}
            for item in running:
                x[item["_id"]] = str(
                    (item["files"]["completed"] / item["files"]["total"]) * 100)

            yield "data:" + json.dumps(x) + "\n\n"
            time.sleep(1)

    return Response(generate(), mimetype='text/event-stream')


app.add_url_rule("/", endpoint="dashboard", view_func=index, methods=['GET'])
app.add_url_rule("/newScan", endpoint="newScan",
                 view_func=new_scan, methods=['GET'])
app.add_url_rule("/progress", endpoint="progress",
                 view_func=progress, methods=['GET'])
