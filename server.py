from flask import Flask, request
from flask_cors import CORS
from video_capture import VideoCapture
import threading
import os
import logging

app = Flask(__name__)
CORS(app)
vc = VideoCapture()
logging.basicConfig(level=logging.INFO)


def remove(file):
    try:
        os.remove(file)
    except OSError as e:
        logging.error(f"Error removing file {file}: {e}")


@app.route('/', methods=['GET'])
def index():
    return {}, 200


@app.route('/configure', methods=['GET'])
def configure():
    url = request.args.get('url')
    video_source = request.args.get('video_source', '0')

    if url:
        vc.url = url

    if video_source:
        try:
            vc.configure_video_source(int(video_source))
        except ValueError:
            logger.error(f"Invalid video source: {video_source}, needs to be an integer")
            return { "error": "video_source must be integer" }, 400

    return {}, 200


@app.route('/start', methods=['GET'])
def start():
    vc.run = True
    threading.Thread(target=vc.start, daemon=True).start()
    logging.info('Started')
    return {}, 200


@app.route('/stop', methods=['GET'])
def stop():
    vc.run = False
    if request.args.get('clean', 'false').lower() == 'true':
        logging.info('Cleaning up...')
        while vc.files:
            file = vc.files.pop()
            threading.Thread(target=remove, args=(file,), daemon=True).start()
    logging.info('Stopped')
    return {}, 200


if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = os.getenv('FLASK_PORT', 5001)
    app.run(host=host, port=port, debug=bool(os.getenv('FLASK_DEBUG', False)))
