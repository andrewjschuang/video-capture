import cv2
import threading
import requests
import time
import os
from PIL import Image
from io import BytesIO

video_source = os.getenv('VIDEO_SOURCE', 0)
url = os.getenv('BMSISP', 'http://localhost:5000')

def send(filename):
    print('sending frame')
    try:
        img = open(filename, 'rb')
        r = requests.post(url, files={'file': img})
        img.close()
        threading.Thread(target=os.remove, args=(filename,)).start()
        print('frame sent. status code: %s' % r.status_code)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    try:
        video_source = int(video_source)
    except:
        pass

    video_capture = cv2.VideoCapture(video_source)
    if not video_capture.isOpened():
        print('error opening video source %s' % video_source)
        exit(1)

    n = 0
    while True:
        ret, frame = video_capture.read()
        if ret:
            print('got new frame')
            pil_image = Image.fromarray(frame)
            filename = 'frames/img' + str(n) + '.jpg'
            pil_image.save(filename)
            threading.Thread(target=send, args=(filename,)).start()
            n += 1
        time.sleep(0.5)
