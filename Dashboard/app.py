from flask import Flask, render_template, request, redirect, url_for, Response
from datetime import datetime
from werkzeug.utils import secure_filename
import os
import uuid
from pymongo import MongoClient
import json
from hurry.filesize import size, si
from dotenv import load_dotenv
from flask_cors import CORS
from redis import Redis
from threading import Thread

load_dotenv()

app = Flask(__name__)
CORS(app,resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app, message_queue=os.environ.get('REDIS_URL'),cors_allowed_origins='*')


app.config['UPLOAD_FOLDER'] = os.getenv("UPLOAD_DIRECTORY")

mongodbHost = os.getenv("MONGODB_HOST")
mongodbPort = int(os.getenv("MONGODB_PORT"))

client = MongoClient(mongodbHost, mongodbPort)
scan8 = client['scan8']
prequeuedScans = scan8['prequeuedScans']
queuedScans = scan8['queuedScans']
runningScans = scan8['runningScans']
completedScans = scan8['completedScans']

redis_client = Redis(host=os.getenv('REDIS_HOST'),port=int(os.getenv("REDIS_PORT")))
redis_pubsub = redis_client.pubsub()
redis_pubsub.subscribe('scan_progress')

# Socket implementation
def background_thread():

    def parse_message(message):
        json_str = message.decode('utf-8')
        return json.loads(json_str)

    for message in redis_pubsub.listen():
        if message['type'] == 'message':
            json_data = parse_message(message['data'])
            socketio.emit('update', {'data': json_data})

@socketio.on('connect')
def connect():
    print("Started background thread")
    thread = Thread(target=background_thread)
    thread.daemon = True
    thread.start()

def index():
    prequeued = prequeuedScans.find()
    queued = queuedScans.find()
    running = runningScans.find()
    completed = completedScans.find()
    return render_template('index.html', prequeued=prequeued, queued=queued, running=running, completed=completed, newScanUrl=url_for('newScan'))


def new_scan():
    return render_template('newScan.html')

def upload_files():
    if request.method == 'POST':
        id = uuid.uuid4()
        uploadedFiles = request.files.getlist('dir')
        dirPath = os.path.join(app.config['UPLOAD_FOLDER'], str(id))
        os.mkdir(dirPath)

        for file in uploadedFiles:
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(dirPath, filename))

        curTime = datetime.now()
        dirSize = 0
        numFiles = 0
        for element in os.scandir(dirPath):
            dirSize+=os.path.getsize(element)
            numFiles += 1
            
        scan8.prequeuedScans.insert_one(
            {"_id": str(id), "submitTime": {"date": curTime.strftime("%d-%m-%Y"), "time": curTime.strftime(
                "%H:%M:%S")}, "size": size(dirSize, system=si), "files": {"total": numFiles, "completed": 0}}
        )

    return redirect(url_for('dashboard'))


def progress():
    def generate():
        while True:
            running = runningScans.find()
            x = {}
            for item in running:
                x[item["_id"]] = str(
                    (item["files"]["completed"] / item["files"]["total"]) * 100)

            yield "data:" + json.dumps(x) + "\n\n"

    return Response(generate(), mimetype='text/event-stream')


app.add_url_rule("/", endpoint="dashboard", view_func=index, methods=['GET'])
app.add_url_rule("/newScan", endpoint="newScan",
                 view_func=new_scan, methods=['GET'])
app.add_url_rule("/progress", endpoint="progress",
                 view_func=progress, methods=['GET'])
app.add_url_rule("/upload", endpoint="upload",
                 view_func=upload_files, methods=['GET', 'POST'])

if __name__ == "__main__":
    app.debug = True
    socketio.run(app, log_output=True)
   
