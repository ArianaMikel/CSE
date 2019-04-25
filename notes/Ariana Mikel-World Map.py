world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's Room",
        'DESCRIPTION': "This is the classroom you are in right now. "
                       "There are two doors on the north wall",
        'PATHS': {
            'NORTH': "PARKING_LOT",
            'SOUTH': "FLOOD_ROOM",
            'EAST': "DEATH_ROOM"

            }
    },
    'PARKING_LOT': {
        'NAME': "The North Parking Lot",
        'DESCRIPTION': "There are a couple cars parked here.",
        'PATHS': {
            'SOUTH': 'R19A',
            'EAST': "RICO'S_FOOD_TRUCK"

             }
    },
    "RICO'S_FOOD_TRUCK": {
        'NAME': "Rico's Food Truck",
        'DESCRIPTION': "This truck is filled with light and it has 'La Chona' playing on the speakers."
                       "Try to get some tacos to load up on energy!",
        'PATHS': {
            'SOUTH': 'DEATH_ROOM',
            'WEST': 'PARKING_LOT',
            'EAST': 'RED_FOREST'

        }
    },
    "DEATH_ROOM": {
        'NAME': "Death Room",
        'DESCRIPTION': "Why did you come here? Sis finna die :(",

        'PATHS': {
            'SOUTH': 'GROCERY_STORE',
            'WEST': 'R19A',
            'EAST': 'SUGAR_FOREST'

        }
    },
    "SUGAR_FOREST": {
        'NAME': "Sugar Forest",
        'DESCRIPTION': "This place is covered with all things sugary, cookies, cakes, and donuts oh my. "
                       "Try to grab some donuts to get energy",

        'PATHS': {
            'NORTH': 'RED_FOREST',
            'WEST': 'DEATH_ROOM',
            'EAST': 'MAGICAL_CASTLE',
            'SOUTH': 'BLUE_FOREST'

        }
    },
    "RED_FOREST": {
        'NAME': "Red Forest",
        'DESCRIPTION': "The trees have all red leaves and some fell on the floor"
                       "All you can hear is the sound of birds chirping",

        'PATHS': {
            'SOUTH': 'SUGAR_FOREST',
            'WEST': "RICO'S_FOOD_TRUCK",
            'EAST': "GOBLIN'S_LAIR"

        }
    },
    "GOBLIN'S_LAIR": {
        'NAME': "Goblin's Lair",
        'DESCRIPTION': "It smells like burnt rubber and cow scat",

        'PATHS': {
            'SOUTH': 'MAGICAL_CASTLE',
            'WEST': 'RED_FOREST',
            'NORTH': 'QUEST_ROOM'

        }
    },
    "MAGICAL_CASTLE": {
        'NAME': "Magical Castle",
        'DESCRIPTION': "The smell of sweet roses is in the air, as you walk into the castle, everything is white."
                       "You walk into the grand ballroom, everything is perfect",

        'PATHS': {
            'SOUTH': "OGRE'S LAIR",
            'NORTH': "GOBLIN'S LAIR",
            'EAST': 'UPDATE_ROOM_1',
            'WEST': 'SUGAR_FOREST'

        }
    },
    "UPDATE_ROOM_1": {
        'NAME': "Update Room #1",
        'DESCRIPTION': "As you come in you see a vortex, you walk closer and look inside it",

        'PATHS': {
            'SOUTH': "QUEST_ROOM",
            'NORTH': "QUEST_ROOM",
            'EAST': 'MAGICAL_CASTLE',
            'WEST': 'QUEST_ROOM'

        }
    },
    "OGRE'S_LAIR": {
        'NAME': "Ogre's Lair",
        'DESCRIPTION': "It's dark ans smells like moldy milk. A hairy Orge emerges from the darkness",

        'PATHS': {
            'DOWN': "HELL",
            'NORTH': "MAGICAL_CASTLE",
            'WEST': 'BLUE_FOREST'

        }
    },
    "BLUE_FOREST": {
        'NAME': "Blue Field",
        'DESCRIPTION': "The blue sky, the river and the field full of blue orchids",

        'PATHS': {
            'NORTH': "SUGAR_FOREST",
            'WEST': 'GROCERY_STORE',
            'EAST': "OGRE'S_LAIR"

        }
    },
    "GROCERY_STORE": {
        'NAME': "Grocery Store",
        'DESCRIPTION': "You can smell the sweet smells of the bakery and the greasy smells of the food court. The "
                       "aisles are perfectly parallel to each other",

        'PATHS': {
            'NORTH': "DEATH_ROOM",
            'WEST': 'FLOOD_ROOM',
            'EAST': "BLUE_FOREST"

        }
    },
    "FLOOD_ROOM": {
        'NAME': "Flood Room",
        'DESCRIPTION': "As you go in water is at your feet. Your shoes are now soggy.",

        'PATHS': {
            'NORTH': "R19A",
            'EAST': "GROCERY_STORE"

        }
    },
    "HELL": {
        'NAME': "The Entrance to Hell",
        'DESCRIPTION': "The flames start to reach your skin, you start to smell your own burning flesh.",

        'PATHS': {
            'NORTH': "OGRE'S_LAIR",
            'WEST': "DEAD_PUPPY_ROOM"

        }
    },
    "DEAD_PUPPY_ROOM": {
        'NAME': "Dead Puppy Room",
        'DESCRIPTION': "Puppy skulls, puppy guts and the smell of decaying canines.",

        'PATHS': {
            'EAST': "HELL",
            'WEST': "'MEETING_THE_PARENTS'"

        }
    },
    "QUEST_ROOM": {
        'NAME': "Quest Room",
        'DESCRIPTION': "",

        'PATHS': {
            'EAST': "HELL",
            'WEST': "'MEETING_THE_PARENTS'"

        }
    },
}

# Controller
playing = True
current_node = world_map['R19A']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']
while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
       try:
        room_name = current_node['PATHS'][command]
        current_node = world_map[room_name]
       except KeyError:
           print("I can't go that way")
    else:
        print("Command not found")

