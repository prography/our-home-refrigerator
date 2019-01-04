from flask import Flask, request
import socket
from userMange.login import login
import json
from config.config import get_config
import os
import numpy as np
import cv2

app = Flask(__name__)


@app.route('/')
def index_page():
    return 'hi'


@app.route('/detect', methods=['GET', 'POST'])
def detect_page():
    req = request
    nparr = np.fromstring(req.data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return 'complete'


@app.route('/login')
def login_page():
    req = request.get_json(force=True)
    num, id = login(req, config.user_info_dir, config.user_info_db)
    data = {}
    data[config.user_id_name] = id
    return json.dumps(data, ensure_ascii=False)


@app.route('/camera')
def camera_page():
    pass

if __name__ == '__main__':
    IP = str(socket.gethostbyname(socket.gethostname()))
    config = get_config()
    app.run(host=IP, debug=True, port=12345)

