from flask import Flask, request
import socket
from userMange.login import login
import json
from config.config import get_config
import os
import numpy as np
import cv2
from detection.switch.switch import switch
from detection.switch.delete import delete_user_command
from userMange.register import register

app = Flask(__name__)


@app.route('/')
def index_page():
    return 'hi'


@app.route('/check_command', methods=['POST'])
def check_command():
    req = request.get_json(force=True)
    res = delete_user_command(req)
    print(res)
    return str(res)


@app.route('/detect', methods=['POST'])
def detect_page():
    req = request
    nparr = np.fromstring(req.data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    print(img)
    return 'complete'


@app.route('/login', methods=['POST'])
def login_page():
    req = request.get_json(force=True)
    num, id = login(req, config.user_info_dir, config.user_info_db)
    if num == False:
        num, id = register(req, config.user_info_dir, config.user_info_db)
        print("[*] create information of raspberry pi")
    data = {}
    data[config.user_id_name] = id
    return json.dumps(data, ensure_ascii=False)


@app.route('/camera', methods=['POST'])
def camera_page():
    req = request.get_json(force=True)
    return str(switch(req))


if __name__ == '__main__':
    IP = str(socket.gethostbyname(socket.gethostname()))
    config = get_config()
    app.run(host=IP, debug=True, port=12345)

