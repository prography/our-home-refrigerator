import cv2
import os


def imgCap():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        raise Exception("Camera is not found")

    if not os.path.exists('temp'):
        os.makedirs('temp')

    ret, img = cam.read()
    while not ret:
        ret, img = cam.read()
    img = cv2.flip(img, 1)
    cv2.imwrite(os.path.join('temp', 'new.PNG'), img)

    img = cv2.imread(os.path.join('temp', 'new.PNG'), cv2.IMREAD_COLOR)

    content_type = 'image/PNG'
    headers = {'content-type': content_type}
    print(img)
    _, img_encoded = cv2.imencode('.PNG', img)

    if not os.path.exists('temp'):
        os.makedirs('temp')

    return headers, img_encoded
