import React, {Component} from 'react'
import {Launcher} from 'react-chat-window'
import './chatbox.css'

class ChatBox extends React.Component {
  
  constructor() {
    super();
    this.state = {
      messageList: [],
      _isOpen: false
    };
  }
  

  _onMessageWasSent(message) {
    this.setState({
      messageList: [...this.state.messageList, message]
    })
  }

  _sendMyMessage(text) {
    if(this.state._isOpen) {
      if (text.length > 0) {
        this.setState({
          messageList: [...this.state.messageList, {
            author: 'me',
            type: 'text',
            data: { text }
          }]
        })
      }
    }
    
  }

  _sendMessage(text) {
    if(this.state._isOpen) {
      if (text.length > 0) {
        this.setState({
          messageList: [...this.state.messageList, {
            author: 'them',
            type: 'text',
            data: { text }
          }]
        })
      }
    }
  }

  _handleClick() {
    this.setState({
      _isOpen: !this.state._isOpen
    })
  }

  render() {
    return (<div>
      <Launcher
        agentProfile={{
          teamName: 'Conversation',
          imageUrl: 'https://a.slack-edge.com/66f9/img/avatars-teams/ava_0001-34.png'
        }}
        onMessageWasSent={this._onMessageWasSent.bind(this)}
        messageList={this.state.messageList}
        showEmoji
        mute={true}
        showEmoji={false}
        isOpen={this.state._isOpen}
        handleClick={this._handleClick.bind(this)}
      />
    </div>)
  }
}

export default ChatBox