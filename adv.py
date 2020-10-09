from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Stack
from helpers import add_room_to_map, get_unexplored_direction, get_opposite_direction

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

##########################################################################################################

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
room_map = {}
room_map = add_room_to_map(room_map, player.current_room)

s = Stack()

traversal_path = []

while len(room_map) < len(world.rooms):

    # while there is an unexplored direction, move that way and log it to the map and the traversal path
    while get_unexplored_direction(room_map, player.current_room):
        if len(room_map) == len(world.rooms):
            break
        
        direction = get_unexplored_direction(room_map, player.current_room)
        old_room = player.current_room

        s.push(get_opposite_direction(direction))

        if direction is not None: 
            player.travel(direction)

        if player.current_room.id not in room_map:
            add_room_to_map(room_map, player.current_room)

        room_map[player.current_room.id][get_opposite_direction(direction)] = old_room.id
        room_map[old_room.id][direction] = player.current_room.id

        traversal_path.append(direction)

    # go back to a room with an unexplored direction
    while get_unexplored_direction(room_map, player.current_room) is None and s.size() > 0:   
        if len(room_map) == len(world.rooms):
            break

        direction = s.pop()
        if direction is not None: 
            player.travel(direction)
        traversal_path.append(direction)

# print(traversal_path)
# print(room_map)

##########################################################################################################

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
