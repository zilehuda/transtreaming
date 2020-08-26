import json
from helpers import constants
import os

def get_user_objs(roomid, uid):
    user_objs = []
    if os.path.exists(constants.ROOMS_FILENAME):
        with open(constants.ROOMS_FILENAME, 'r') as rooms_file:
            rooms = json.load(rooms_file)
        if isinstance(rooms, dict):
            if roomid in rooms:
                room = rooms[roomid]
                users = room["users"]
                for k,v in users.items():
                    if k != uid:
                        user_objs.append({
                            "partner_id": k,
                            "language": users[k]["language"]
                        })
    return user_objs

