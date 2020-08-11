from flask import Flask, request, flash, redirect
from rest.v1.user import app as user_api_v1
from rest.v1.transcripe_and_translate import app as tat_api_v1
from flask_socketio import SocketIO, emit
import json
from helpers import converter as converter_helper, user as user_helper


UPLOAD_FOLDER = '/temp'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
socketio = SocketIO(app, cors_allowed_origins="*")

app.register_blueprint(user_api_v1, url_prefix="/v1")
app.register_blueprint(tat_api_v1, url_prefix="/v1")

@socketio.on('connect')
def handle_connect():
    print('Client connected')

# {
#     "text": "",
#     "roomid: "",
#     "partner_id": "",
#     "src": "en"
# }
@socketio.on('translate')
def translate(body):
    text = body["text"]
    roomid = body["roomid"]
    partner_id = body["partner_id"]
    src = body["src"]

    user_obj = user_helper.get_user_obj(roomid, partner_id)
    if user_obj is not None:
        destination_language = user_obj["language"]

        translated_text = converter_helper.convert_text_to_lang(text, src, destination_language)
        translate_and_transmit(partner_id, translated_text)


def translate_and_transmit(socket_channel, text):
    emit(socket_channel, text)



if __name__ == "__main__":
    app.run()
    socketio.run(app)