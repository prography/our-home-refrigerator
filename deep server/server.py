from flask import Flask, request
import socket
import os
app = Flask(__name__)


@app.route('/')
def index():
    return


@app.route('/detect')
def detect():
    return


@app.route('/login')
def login():
    req = request.get_json(force=True)
    return


if __name__ == '__main__':

    IP = str(socket.gethostbyname(socket.gethostname()))
    app.run(host=IP, debug=True, port=12345)