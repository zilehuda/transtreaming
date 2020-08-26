from flask import Flask, request, flash, redirect, Blueprint
from helpers import file as file_helper, converter as converter_helper, constants

app = Blueprint('transcribe_and_translate', __name__)


@app.route("/transcripe_and_translate", methods=["POST"])                   
def transcripe_and_translate():
    if request.method == 'POST':
        response = None
        source = request.form.get("source", None)
        destination = request.form.get("destination", None)
        if source is None or destination is None:
            return {"status": 400, "message": "source or destination is not defined"}
        filename = file_helper.save_file(request)
        if filename:
            wav_to_text = converter_helper.convert_text_from_audio(filename)
            if wav_to_text:
                translated_text = converter_helper.convert_text_to_lang(wav_to_text, source, destination)
                if translated_text:
                    response =  {"status": 200, "translated_text": translated_text}
                else:
                    response =  {"status": 400, "message": "Something went wrong in translating"}
            else:
                response =  {"status": 400, "message": "Something went wrong in transcribing"}
        else:
            response =  {"status": 400, "message": "Something went wrong with audio"}

        file_helper.remove_file(filename)
        return response

@app.route("/languages", methods=["GET"])                   
def get_languages():
    languages = constants.LANGUAGES
    return {
        "status": 200,
        "languages": languages
    }

@app.route("/translate", methods=["GET"])                   
def get_translated_text():
    response = None
    source = request.form.get("source", None)
    destination = request.form.get("destination", None)
    text = request.form.get("text", None)
    if source is None or destination is None or text is None:
        return {"status": 400, "message": "source or destination is not defined"}

    translated_text = converter_helper.convert_text_to_lang(text, source, destination)
    if translated_text:
        response =  {"status": 200, "translated_text": translated_text}
    else:
        response =  {"status": 400, "message": "Something went wrong in translating"}
    return response