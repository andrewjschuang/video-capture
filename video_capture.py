import cv2
import threading
import requests
import time
import os
from PIL import Image

video_source = os.getenv('VIDEO_SOURCE', 0)
url = os.getenv('BMSISP', 'http://localhost:5000')

def send(image):
    print('sending frame')
    try:
        r = requests.post(url, files={'file': image})
        print('frame sent. status code: %s' % r.status_code)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    try:
        os.mkdir('frames')
    except:
        pass

    video_capture = cv2.VideoCapture(video_source)
    if not video_capture.isOpened():
        exit(1)

    while True:
        ret, frame = video_capture.read()
        if ret:
            print('got new frame')
            pil_image = Image.fromarray(frame)
            threading.Thread(target=send, args=(pil_image.tobytes(),)).start()
        time.sleep(0.5)
