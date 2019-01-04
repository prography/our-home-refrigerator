import requests
import cv2
import os
from imgCap import imgCap


URL = 'http://192.168.35.220:12345/detect'
headers, img_encoded= imgCap()
response = requests.post(URL, data=img_encoded.tostring(), headers=headers)

