import React from "react";
import * as Cookies from "js-cookie";
import axios from 'axios';

import "./meeting.css";
import AgoraVideoCall from "../../components/AgoraVideoCall";
import SpeechToText  from '../../components/SpeechToText/index';
import ChatBox from '../../components/ChatBox/index';
import socketIOClient from "socket.io-client";
require('dotenv').config()
const socket = socketIOClient(process.env.REACT_APP_EUROPA_BASE_URL);

require('dotenv').config()



class Meeting extends React.Component {
  
  constructor(props) {
    super(props);
    this.videoProfile = Cookies.get("videoProfile").split(",")[0] || "480p_4";
    this.channel = Cookies.get("channel") || "test";
    this.transcode = Cookies.get("transcode") || "interop";
    this.attendeeMode = Cookies.get("attendeeMode") || "video";
    this.baseMode = Cookies.get("baseMode") || "avc";
    this.language = Cookies.get("language") || "en";
    this.myText = undefined
    
    this.appId = process.env.REACT_APP_AGORA_APP_ID;
    if (!this.appId) {
      return alert("Get App ID first!");
    }
    // this.uid = undefined
    this.uid = Math.random().toString(36).substring(7);

    var data = {
      "uid": this.uid,
      "roomid": this.channel,
      "language": this.language
    }
    axios({
      method: 'post',
      url: process.env.REACT_APP_EUROPA_BASE_URL + '/v1/users',
      data: data,
      headers: {'Content-Type': 'application/json' , 'Access-Control-Allow-Origin': '*'}
      })
      .then(function (response) {
          //handle success
          console.log(response);
      })
      .catch(function (response) {
          //handle error
          console.log(response);
      });
   
  socket.on(this.uid, (data) => {
    console.log("translated", data);
    const translated_text_string = data.translated_text;
      this.handlepartnerText(translated_text_string)
      // setTranslatedText(translated_text_string)
      // setTranslatedText(undefined)
  });
  }
  

  handlemyText = (textValue) => {
    this.refs.chatBox._sendMyMessage(textValue)
  }

  handlepartnerText = (textValue) => {
    this.refs.chatBox._sendMessage(textValue)
  }

  render() {
    return (
      <div className="wrapper meeting">
        <div className="ag-header">
          <div className="ag-header-lead">
            <img
              className="header-logo"
              src={require("../../assets/images/transtreaming-logo.png")}
              alt=""
            />
            
          </div>
          <div className="ag-header-msg">
            Room ID:&nbsp;<span id="room-name">{this.channel}</span>
          </div>
        </div>
        <div className="ag-main">
          
          <div className="ag-container">
            <AgoraVideoCall
              videoProfile={this.videoProfile}
              channel={this.channel}
              transcode={this.transcode}
              attendeeMode={this.attendeeMode}
              baseMode={this.baseMode}
              appId={this.appId}
              uid={this.uid}
            />
          </div>
          <div >
            <SpeechToText
            uid={this.uid}
            language={this.language}
            roomid={this.channel}
            onSetmyText={this.handlemyText.bind(this)}
            onSetpartnerText={this.handlepartnerText.bind(this)}
            />
            </div>
          </div>
          
        <div className="ag-footer">
          <a className="ag-href" href="https://www.agora.io">
            <span>Powered By Agora</span>
          </a>
          {/* <span>Talk to Support: 400 632 6626</span> */}
        </div>
        <ChatBox
          ref="chatBox"
         />
      </div>
    );
  }
}

export default Meeting;
