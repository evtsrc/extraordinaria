from flask import Flask
from datetime import datetime
import socket
import os

PORT = os.getenv('PORT')
MESSAGE = "Kaixo!\n"
HEALTH = "Healthy!\n"

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result

@app.route("/healthz")
def healthz():
    result = HEALTH.encode("utf-8")
    return result

@app.route("/hostname")
def hostname():
    HOST = socket.gethostname()+"\n"
    result = HOST.encode("utf-8")
    return result

@app.route("/write")
def write():
    f = open("/data/access.txt", "a")
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    f.write(date_time + " - El host " + socket.gethostname() + " ha escrito aquí!\n")
    f.close()

    return "OK\n".encode("utf-8")

@app.route("/read")
def read():
    f = open("/data/access.txt", "r")
    return f.read()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
