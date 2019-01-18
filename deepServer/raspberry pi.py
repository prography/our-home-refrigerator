import requests
import cv2
import os
from imgCap import imgCap
from config.config import get_config

config = get_config()


detect_URL = 'http://192.168.118.1:12345/detect'
login_URL = "http://192.168.118.1:12345/login"

id = {}
id[config.user_id_name] = 'AVDF'

'''response = requests.post(login_URL, json=id)'''

headers, img_encoded= imgCap()
response = requests.post(detect_URL, data=img_encoded.tostring(), headers=headers)

