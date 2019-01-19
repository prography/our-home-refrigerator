import requests
import cv2
import os
from imgCap import imgCap
from config.config import get_config
from time import sleep
import json
import urllib3
config = get_config()

id = {}
check = ''
id[config.user_id_name] = 'AVDF'
detect_URL = 'http://192.168.118.1:12345/detect'
login_URL = "http://192.168.118.1:12345/login"
command_URL = 'http://192.168.118.1:12345/check_command'

# wire raspberry pi on server
response = requests.post(login_URL, json=id)

while True:
    # check command of raspberry pi
    check = requests.post(command_URL, json=id)
    print(check.text)
    if str(check.text) == id[config.user_id_name]:
        print('activate camera')
        # Transmit image
        headers, img_encoded = imgCap()
        response = requests.post(detect_URL, data=img_encoded.tostring(), headers=headers)
    sleep(1)
