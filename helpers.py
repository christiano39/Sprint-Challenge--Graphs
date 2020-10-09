import random

def add_room_to_map(room_map, room):
    room_map[room.id] = {}
    
    for direction in room.get_exits():
        room_map[room.id][direction] = '?'

    return room_map

# def get_unexplored_direction(room_map, room):
#     for direction in room_map[room.id]:
#         if room_map[room.id][direction] == '?':
#             return direction

#     return None

def get_unexplored_direction(room_map, room):
    dirs = []
    
    for direction in room_map[room.id]:
        if room_map[room.id][direction] == '?':
            dirs.append(direction)

    if len(dirs) == 0: return None

    return random.choice(dirs)

def get_opposite_direction(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'e':
        return 'w'
    elif direction == 'w':
        return 'e'
    
    return None