from flask import Flask, request, flash, redirect
from rest.v1.user import app as user_api_v1
from rest.v1.transcripe_and_translate import app as tat_api_v1
from flask_socketio import SocketIO, emit
import json
from helpers import converter as converter_helper, user as user_helper
from flask_cors import CORS, cross_origin
import base64
import chardet


UPLOAD_FOLDER = '/temp'
app = Flask(__name__)
CORS(app, resources= {
    r"/*": {
        "origins": "*"
    }
}, allow_headers='*', origins='*')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
socketio = SocketIO(app, cors_allowed_origins="*")

app.register_blueprint(user_api_v1, url_prefix="/v1")
app.register_blueprint(tat_api_v1, url_prefix="/v1")

# @app.route('/test')
# def Emm():
#     print("DDDDDDDDDDDDDDDDDDDdddd")
#     translate_and_transmit("nye1lk", "working")
#     return "D"

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
    uid = body["uid"]
    src = body["src"]

    user_objs = user_helper.get_user_objs(roomid, uid)

    if len(user_objs) > 0:
        for user_obj in user_objs:
            partner_id = user_obj['partner_id']
            destination_language = user_obj["language"]
            translated_text = converter_helper.convert_text_to_lang(text, src, destination_language)
            translate_and_transmit(partner_id, translated_text)


def translate_and_transmit(socket_channel, text):
    print(socket_channel, text)
    response = {
        "translated_text": text
    }
    socketio.emit(socket_channel, response)



if __name__ == "__main__":
    app.run()
    socketio.run(app)