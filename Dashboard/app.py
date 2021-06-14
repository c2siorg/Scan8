from flask import Flask, render_template

app = Flask(__name__)

# TODO: add a caching layer to all routes


def index():
    # TODO: connect mongoDB and retrieve data to lists

    queued = [
        {"scanNo": "--", "submitTime": "01-01-2000 12:00:00",
            "size": "--", "numFiles": "--", "stats": "0"},
        {"scanNo": "--", "submitTime": "01-02-2000 01:00:00",
            "size": "--", "numFiles": "--", "stats": "0"},
        {"scanNo": "--", "submitTime": "01-03-2000 02:00:00",
            "size": "--", "numFiles": "--", "stats": "0"}
    ]
    running = [
        {"scanNo": "1", "submitTime": "02-02-2001 13:00:00",
            "size": "4GB", "numFiles": "100", "stats": "50"},
        {"scanNo": "2", "submitTime": "03-03-2002 14:00:00",
            "size": "1GB", "numFiles": "10", "stats": "75"}
    ]
    completed = [{"scanNo": "4", "submitTime": "04-04-2004 14:00:00",
                  "size": "9GB", "numFiles": "1000", "stats": "100"}]

    return render_template('index.html', queued=queued, running=running, completed=completed)


def new_scan():
    return render_template('newScan.html')


app.add_url_rule("/", endpoint="dashboard", view_func=index, methods=['GET'])
app.add_url_rule("/newScan", endpoint="newScan",
                 view_func=new_scan, methods=['GET'])
