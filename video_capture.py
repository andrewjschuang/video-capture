import cv2
import threading
import requests
import time
import os
import random
from PIL import Image

class VideoCapture():
    def __init__(self, url='http://localhost:5000/api', video_source=0):
        try:
            os.mkdir('frames')
        except:
            pass
        self.files = ['frames/' + x for x in os.listdir('frames')]
        self.run = True
        self.url = url
        self.video_capture = cv2.VideoCapture(video_source)

    def configure(self, video_source):
        self.video_capture.release()
        try:
            self.video_capture = cv2.VideoCapture(video_source)
            if not self.video_capture.isOpened():
                print('error opening video source %s' % video_source)
                exit(1)
        except:
            print('couldnt configure video_source')

    def start(self, sleep=0.5):
        while self.run:
            ret, frame = self.video_capture.read()
            if ret:
                print('got new frame')
                pil_image = Image.fromarray(frame)
                filename = f'frames/{time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())}.jpg'
                pil_image.save(filename)
                self.files.append(filename)
                threading.Thread(target=self.send, args=(filename,)).start()
            time.sleep(sleep)

    def send(self, f):
        print('sending frame')
        try:
            with open(f, 'rb') as img:
                r = requests.post(self.url, files={'file': img})
                print(r.text)
        except Exception as e:
            print(e)
