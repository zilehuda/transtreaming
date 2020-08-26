from flask import Blueprint, request
from helpers import constants
import json
import os


app = Blueprint('user_api', __name__)

#TODO: room.json is the temporary solution for maintaining the users and rooms
@app.route("/users", methods=["POST"])                   
def user():
    data = request.get_json()
    uid = data.get('uid')
    roomid = data.get("roomid")
    language = data.get("language")
    if uid is None or roomid is None or language is None:
        return {"status": 400, "message": "uid or roomid or language is not defined"}

    if os.path.exists(constants.ROOMS_FILENAME) == False:
        with open(constants.ROOMS_FILENAME, 'w') as file:
            file.write(json.dumps({}))

    with open(constants.ROOMS_FILENAME, 'r') as rooms_file:
        rooms = json.load(rooms_file)
    
    if isinstance(rooms, dict):
        if roomid in rooms:
            print("I AM EXIST")
            room = rooms[roomid]
            users = room["users"]
            user_object = {
                "language": language
            }
            users[uid] = user_object
            rooms[roomid] = {
                "users": users
            }
        else:
            print("I am not exist")
            user_object = {}
            users = {}
            user_object = {
                "language": language
            }
            users[uid] = user_object
            rooms[roomid] = {
                "users": users
            }

        with open(constants.ROOMS_FILENAME, 'w') as room_file:
            json.dump(rooms, room_file)
    return rooms
