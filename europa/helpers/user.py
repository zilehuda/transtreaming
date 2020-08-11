import json
from helpers import constants
import os

def get_user_obj(roomid, userid):
    user_obj = None
    if os.path.exists(constants.ROOMS_FILENAME):
        with open(constants.ROOMS_FILENAME, 'r') as rooms_file:
            rooms = json.load(rooms_file)
        if isinstance(rooms, dict):
            if roomid in rooms:
                print("Room", rooms)
                room = rooms[roomid]
                users = room["users"]
                if userid in users:
                    user_obj = users[userid]
    return user_obj

