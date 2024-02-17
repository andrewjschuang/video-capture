import cv2
import threading
import requests
import time
import os
import logging
from PIL import Image
from queue import Queue

logging.basicConfig(level=logging.INFO)


class VideoCapture():
    def __init__(self, url="http://localhost:5000/api", video_source=0):
        self.ensure_directory_exists('frames')
        self.files = ['frames/' + x for x in os.listdir('frames')]
        self.run = True
        self.url = url
        self.video_source = video_source
        self.video_capture = self.initialize_video_capture(video_source)
        self.frame_queue = Queue()
        self.sender_thread = threading.Thread(target=self.send_frames, daemon=True)
        self.sender_thread.start()


    def ensure_directory_exists(self, directory):
        if not os.path.exists(directory):
            try:
                os.mkdir(directory)
            except FileExistsError:
                pass  # Directory already exists


    def initialize_video_capture(self, video_source):
        video_capture = cv2.VideoCapture(video_source)
        if not video_capture.isOpened():
            logging.error(f"Error opening video source {video_source}")
            raise ValueError(f"Error opening video source {video_source}")
        return video_capture


    def configure_video_source(self, video_source):
        self.video_capture.release()
        self.video_capture = self.initialize_video_capture(video_source)


    def start(self, sleep=0.5):
        while self.run:
            ret, frame = self.video_capture.read()
            if ret:
                logging.info('Got new frame')
                current_datetime = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
                file = f'frames/{current_datetime}.jpg'
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                Image.fromarray(rgb_frame).save(file)
                self.files.append(file)
                self.frame_queue.put(file)
            time.sleep(sleep)


    def send_frames(self):
        while self.run or not self.frame_queue.empty():
            file = self.frame_queue.get()
            try:
                with open(file, 'rb') as img:
                    r = requests.post(self.url, files={'file': img})
                    if r.ok:
                        logging.info(f"Sent frame {file}")
                    else:
                        logging.error(f"Error sending frame {file}: {r.status_code} {r.text}")
            except Exception as e:
                logging.error(f"Error sending frame {file}: {e}")
