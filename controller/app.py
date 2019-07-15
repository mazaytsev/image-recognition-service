from threading import Thread

from flask import Flask, request

from service import recognition_service

app = Flask(__name__)


@app.route('/predict')
def main():
    url = request.args.get('img_url', default=1, type=str)
    chat_id = request.args.get('chat_id', default=-1, type=int)
    client_ip = request.host.split(':')[0]
    recogn_thread=Thread(target=recognition_service.recognize_image, args=(url, chat_id, client_ip))
    recogn_thread.start()
    return ('', 200)

if __name__ == '__main__':
    app.run()
