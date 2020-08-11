import speech_recognition as sr
import os
from googletrans import Translator
import time

def convert_text_from_audio(filename):
    r = sr.Recognizer()
    # open the file
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        # audio_data = r.record(source)
        audio_text = r.listen(source)
        # recognize (convert from speech to text)
        # text = r.recognize_google(audio_data)
        # print(text)
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            # using google speech recognition
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            print(text)
            return text
        
        except:
            print('Sorry.. run again...')
            return None

def convert_text_to_lang(text, src, dest):
    try:
        translator = Translator()
        decoded_text = translator.translate(text,src=src, dest=dest)
        print(decoded_text.text)
        return decoded_text.text
    except:
        print("Not able to translate...")
        return None