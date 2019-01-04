from flask import Flask, request
import socket
from userMange.login import login
import json
from config.config import get_config


app = Flask(__name__)

@app.route('/')
def index_page():
    return 'hi'


@app.route('/detect')
def detect_page():
    req = request.get_json(force=True)
    return


@app.route('/login')
def login_page():
    req = request.get_json(force=True)
    num, id = login(req, config.user_info_dir, config.user_info_db)
    data = {}
    data[config.user_id_name] = id
    return json.dumps(data, ensure_ascii=False)


if __name__ == '__main__':
    IP = str(socket.gethostbyname(socket.gethostname()))
    config = get_config()
    app.run(host=IP, debug=True, port=12345)

