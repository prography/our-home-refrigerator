import cv2
import os


def imgCap():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        raise Exception("Camera is not found")

    ret, img = cam.read()
    while not ret:
        ret, img = cam.read()
    img = cv2.flip(img, 1)

    content_type = 'image/PNG'
    headers = {'content-type': content_type}
    _, img_encoded = cv2.imencode('.PNG', img)

    if not os.path.exists('temp'):
        os.makedirs('temp')
    cv2.imwrite(os.path.join('temp', 'new.PNG'), img)

    return headers, img_encoded
