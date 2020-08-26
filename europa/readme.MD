# Europa
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

# Transtreaming Documentation

Please refer to main github reposity for a complete transtreaming documentation
 - [Github Reposity](https://github.com/zilehuda/transtreaming)

# Installation

  Move to europa directory
 ```sh
$ cd europa
```
Create virtual env (optional)

Install the dependencies
 ```sh
$ pip install -r requirements.txt
```

run the flask app
 ```sh
$ python -m flask app.py
```

### Endpoints

| HTTP VERB | DESCRIPTION |ENDPOINT |
| ------ | ------ | ------ |
| GET  | Get languanges |v1/languages |
| POST  | Take the audio, source & destination and translate | v1/transcripe_and_translate |
| POST  | Take the text, source & destination and translate |v1/translate |
| POST  | Take, uid, roomid and language and add the user |v1/users |

### Socket.io

Server Listen on: translate

Receive
```sh
{
    "text": "",
    "roomid: "",
    "uid": "",
    "src": "en"
}
```
Client Listen on: {uid}


Receive
```sh
{
    "translated_text": "hello"
}
```
License
----
This software is licensed under the MIT License (MIT). [View the license](https://github.com/zilehuda/transtreaming-jupiter/blob/master/LICENSE.md).
