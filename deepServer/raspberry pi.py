from flask import Flask, send_file
import cv2
import socket
import os

app = Flask(__name__)

@app.route('/')
def index_page():
    return 'hi'


@app.route('/capture')
def capture_page():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
            return "webcam is not detected"

    ret, image = cam.read()
    while not ret:
        ret, image = cam.read()
    if (ret):
        image = cv2.flip(image, 1)
        if not os.path.exists('./temp'):
            os.makedirs('./temp')
        cv2.imwrite('./temp/new.jpeg', image)
        return send_file('./temp/new.jpeg', mimetype="image/jpeg")  #attachment_filename="new.jpeg", as_attachment=True


if __name__ == '__main__':
    IP = str(socket.gethostbyname(socket.gethostname()))
    app.run(host=IP, debug=True, port=12345)
