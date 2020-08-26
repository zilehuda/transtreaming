import React , { useState } from 'react'
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition'
import socketIOClient from "socket.io-client";
require('dotenv').config()
const socket = socketIOClient(process.env.REACT_APP_EUROPA_BASE_URL);


const SpeechToText = (props) => {
  const { transcript, resetTranscript, interimTranscript, finalTranscript, listening } = useSpeechRecognition()
  const [translatedText, setTranslatedText] = useState(undefined);
  startListening();
  if (!SpeechRecognition.browserSupportsSpeechRecognition()) {
    return null
  }
  const uid = props.uid;
  const roomid = props.roomid;
  const language = props.language;

  function startListening(){
    SpeechRecognition.startListening({ 
        // continuous: true,
        language: props.language,
     })
  }

  // sc-user-input--text

  if (finalTranscript.length > 0) {
      console.log(finalTranscript)
      const temp = finalTranscript;
      resetTranscript()
      console.log("TEMP", temp)
      props.onSetmyText(temp)
      const data = { 
        "roomid": roomid,
        "uid": uid,
        "src": language,
        "text": temp
        }
        socket.emit('translate', data);
  }

  // socket.on(uid, (data) => {
  //       console.log("translated", data);
  //       const translated_text_string = data.translated_text;
  //       if (translated_text_string != translatedText || translatedText === undefined) {
  //         // props.onSetpartnerText(translated_text_string)
  //         setTranslatedText(translated_text_string)
  //         // setTranslatedText(undefined)
  //       }
  // });

  

  

  return (null)
}
export default SpeechToText