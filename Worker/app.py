import os
import sys
import redis
from rq import Worker, Queue, Connection
from dotenv import load_dotenv

load_dotenv()

utilitiesPath = os.getenv("UTILITIES_PATH")

sys.path.insert(0, utilitiesPath)
from scanJob import scan

listen = ['default']

redis_url = os.getenv('REDISTOGO_URL', os.getenv("REDIS_URL"))

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
