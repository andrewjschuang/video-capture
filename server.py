from flask import Flask, request
from video_capture import VideoCapture
import threading
import os

app = Flask(__name__)
vc = VideoCapture()

def remove(f):
    try:
        os.remove(f)
    except:
        pass
    
@app.route('/', methods=['GET'])
def index():
    return 'Use /start or /stop!'

@app.route('/configure', methods=['GET'])
def configure():
    if request.args.get('url'):
        vc.url = request.args.get('url')
    if request.args.get('video_source'):
        try:
            vc.configure(int(request.args.get('video_source')))
        except:
            vc.configure(request.args.get('video_source'))

    return 'configured'

@app.route('/start', methods=['GET'])
def start():
    vc.run = True
    threading.Thread(target=vc.start).start()
    print('started')

    return 'started'

@app.route('/stop', methods=['GET'])
def stop():
    vc.run = False
    print('cleaning up...')
    while len(vc.files) > 0:
        f = vc.files.pop()
        threading.Thread(target=remove, args=(f,)).start()
    print('stopped')

    return 'stopped'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
