# Europa
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


# Installlation

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
$ flask run
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
    "partner_id": "",
    "src": "en"
}
```
Client Listen on: {partner_id}


Receive
```sh
{
    "translated_text": "hello"
}
```
License
----

MIT


**Free Software, Hell Yeah!**
