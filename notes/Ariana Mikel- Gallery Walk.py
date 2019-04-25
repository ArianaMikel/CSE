class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None, west=None, down=None, up=None,
                 move=None, item=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up  # castle_of_ashtree
        self.down = down
        self.move = move
        self.description = description
        self.characters = []
        self.item = item


class Character(object):
    def __init__(self, starting_location):
        self.goblins_lair = starting_location


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """This moves the player to a new room

        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room to see if a room exists in that direction

        :param direction:
        :return: The room object if it exists, or None if it does not
            """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


# Option 2 - Set all at once, modify controller

# Items


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Anvil(Weapon):
    def __init__(self):
        super(Anvil, self).__init__("Anvil", 89)


class DeadPuppy(Weapon):
    def __init__(self):
        super(DeadPuppy, self).__init__("Dead Puppy", 10)


class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__("Keng Sword", 100)


class WoodSword(Sword):
    def __init__(self):
        super(Sword, self).__init__("Wood Sword", 20)


class Armor(Item):
    def __init__(self, name, armor: int):
        super(Armor, self).__init__(name)
        self.armor = armor


class GeneralArmor(Armor):
    def __init__(self):
        super(Armor, self).__init__("General Armor", )


class BestArmor(Armor):
    def __init__(self):
        super(BestArmor, self).__init__("Knight Armor", 100)


class GeneralShield(Armor):
    def __init__(self):
        super(GeneralShield, self).__init__("General Shield", 30)


class KnightShield(Armor):
    def __init__(self):
        super(KnightShield, self).__init__("Knight Shield", 100)


class Food(Item):  # Cookie
    def __init__(self, name):
        super(Food, self).__init__(name)


class Grapes(Food):
    def __init__(self):
        super(Grapes, self).__init__("Grapes")


class Tacos(Food):
    def __init__(self):
        super(Tacos, self).__init__("Tacos")


class Cupcakes(Food):
    def __init__(self):
        super(Cupcakes, self).__init__("Cupcakes")


class Cookies(Food):
    def __init__(self):
        super(Cookies, self).__init__("Cookies")


class Cake(Food):
    def __init__(self):
        super(Cake, self).__init__("Cake")


class Liver(Food):
    def __init__(self):
        super(Liver, self).__init__("Liver")


class Bug(Food):
    def __init__(self):
        super(Bug, self).__init__("Bug")


class Chips(Food):
    def __init__(self):
        super(Chips, self).__init__("Chips")


class GingerAle(Food):
    def __init__(self):
        super(GingerAle, self).__init__("Ginger Ale")


class Ogre(Item):
    def __init__(self):
        super(Ogre, self).__init__("Ogre")


class Goblin(Item):
    def __init__(self):
        super(Goblin, self).__init__("Goblin")


class EvilQueen(Item):
    def __init__(self):
        super(EvilQueen, self).__init__("Evil Queen")


# Characters

anvil = Anvil()
dead_puppy = DeadPuppy()
wood_sword = WoodSword()
sword = Sword()
general_armor = GeneralArmor()
best_armor = BestArmor()
general_shield = GeneralShield()
knight_shield = KnightShield()
grapes = Grapes()
tacos = Tacos()
cupcakes = Cupcakes()
cookies = Cookies()
cake = Cake()
liver = Liver()
bug = Bug()
chips = Chips()
ginger_ale = GingerAle()
goblin = Goblin()
ogre = Ogre()
evil_queeen = EvilQueen()

ricos_food_truck = Room(
    "Rico's Food Truck",
    "This truck is filled with light and it has 'La Chona' playing on "
    "the speakers.Try to get some tacos to load up on energy!", None,
    'death_room', "red_forest", None, None, None, None, sword)
red_forest = Room(
    "Red Forest",
    "The trees have all red leaves and some fell on the floor all you can hear is the sound"
    " of birds chirping", None, "sugar_forest", "goblins_lair",
    "ricos_food_truck")
goblins_lair = Room(
    "Goblin's Lair", "It smells like burnt rubber and cow scat", "quest_room",
    "magical_castle", None, "red_forest", None, None, None, "goblin")
death_room = Room("Death Room", "Why did you come here? Sis finna die :(",
                  "hell", "hell", "hell", "hell")
sugar_forest = Room(
    "Sugar Forest",
    "This place is covered with all things sugary, cookies, cakes, and donuts oh my. "
    "Try to grab some donuts to get energy", "red_forest", "blue_field",
    "magical_castle", "death_room")
magical_castle = Room(
    "Magical Castle",
    "The smell of sweet roses is in the air, as you walk into the castle,"
    " everything is white.You walk into the grand ballroom, everything is perfect",
    "goblins_lair", "ogres_lair", "update_room_1", "sugar_forest")
update_room_1 = Room(
    "Update Room 1",
    "As you come in you see a vortex, you walk closer and look inside it",
    None, None, None, "magical_castle", None, None, "quest_room")
flood_room = Room(
    "Flood Room",
    "As you go in water is at your feet. Your shoes are now soggy.", "R19A",
    None, "grocery_store")
grocery_store = Room(
    "Grocery Store",
    "You can smell the sweet smells of the bakery and the greasy smells of the "
    "food court. The aisles are perfectly parallel to each other. Try to grab some"
    " chips", "death_room", None, "blue_field", "flood_room", None, None, None,
    "grapes"
    " ginger_ale"
    " chips")
blue_field = Room(
    "Blue Field", "The blue sky, the river and the field full of blue orchids",
    "sugar_forest", None, "ogres_lair", "grocery_store")
ogres_lair = Room(
    "Ogre's Lair",
    "It's dark and smells like moldy milk. A hairy Orge emerges from the darkness",
    "magical_castle", None, None, "blue_field", "hell", None, None, "ogre")
hell = Room(
    "Hell",
    "The flames start to reach your skin, you start to smell your own burning flesh.",
    None, None, None, "dead_puppy_room", None, "ogres_lair")
dead_puppy_room = Room(
    "Dead Puppy Room",
    "Puppy skulls, puppy guts and the smell of decaying canines.", None, None,
    "hell", "meet_the_parents", None, None, None, "dead_puppy")
meet_the_parents = Room(
    "Meeting the Parents Room",
    "You walk into a kitchen, there is a man and woman, "
    "they keep asking you about your job and future career", None, None,
    "dead_puppy_room", "hades_lair")
hades_lair = Room(
    "Hades' Lair",
    "Now you are in a dark cave, with a shrine of a red goatman with the fear of thousands"
    " of men in it's eyes", None, None, "meet_the_parents", "update_room_2")
update_room_2 = Room(
    "Update Room 2",
    "Hey there, thanks for going this way, let me take you to the quest storyline.",
    None, None, "hades_lair", None, None, None, "quest_room")
quest_room = Room(
    "Quest Room",
    "Wassup! Listen, you just entered the old town of Old Town, we have a situation, "
    "long story short, you have to save the royal family from an Evil Queen you know easy"
    " "
    "stuff, so have fun and don't die", "old_town", "goblins_lair")
old_town = Room(
    "Old Town",
    "Welcome to the town! Think of wood wheels, throwing your scat out the window and many "
    "diseases."
    "jeybs_blacksmith", "quest_room", "bar", "spooky_forest")
bar = Room(
    "Bar",
    "It smells like ginger ale and old grapes, it is so crowded you cannot take one step without being"
    " shoved, also there are peanut shells covering the floor", None, None,
    None, "old_town")
jeybs_blacksmith = Room(
    "Jeyb's Blacksmith",
    "As you walk in you see swords and other weapons that might come in"
    " use later", None, "old_town", None, None, None, None, None, 'anvil'
    'wood_sword'
    'sword'
    'general_armor'
    'best_armor'
    'general_shield'
    'knight_shield')
fat_boiz_bakery = Room(
    "Fat Boiz Bakery",
    "You can smell the sugar in the air, you see the cupcakes, cookies and cakes",
    "spooky_forest", None, None, None, None, None, None, cupcakes and cookies
    and cake)
spooky_forest = Room(
    "Spooky Forest", "This forest is full of smiles and sunshine",
    "grandmas_house", "fat_boiz_bakery", "old_town", "happy_forest")
grandmas_house = Room(
    "Grandma's House",
    "The house is dark and smells like old fish, there is nothing but spider"
    " webs everywhere", None, "spooky_forest")
happy_forest = Room(
    "Happy Forest",
    "In the trees you can hear the winds blowing harder and harder until you can "
    "barely hear your own thoughts", "ghost_house", "bug_and_liver",
    "spooky_forest", "castle_of_ashtree")
ghost_house = Room(
    "Ghost House",
    "This place is a big white room with an endless suply of food, eat some"
    " but not too much", None, "happy_forest", None, None)
princess_room = Room(
    "Princess Room",
    "You know, just regular princess stuff, black walls with black drapes and "
    "black furniture, with Nirvana, Pink Floyd and Guns'n'Roses posters", None,
    "castle_of_ashtree")
castle_of_ashtree = Room(
    "Castle of Ashtree",
    "The grand off white castle is huge with double doors", "princess_room",
    "k_q_room", "happy_forest", "kitchen")
k_q_room = Room(
    "King and Queen's Room",
    "It smells like roses, with the red and gold room, it is only fit for royalty",
    "castle_of_ashtree")
bug_and_liver = Room(
    "Helga's Bug and Liver Joint",
    "People are passed out on the floor, you can hear children"
    " gag, and it smells like sour fruit", "happy_forest", None, None, None,
    None, None, None, bug and liver)
dungeon = Room("Dungeon",
               "It's dark and wet, you can see cells and skeletons.", None,
               "living_room")
living_room = Room(
    "Living Room",
    "The grand light green living room smells of mint and lime, the furniture is almost"
    " taller that you"
    "dungeon", "kitchen", "castle_of_ashtree", "evil_queen")
kitchen = Room(
    "Kitchen", "Nothing good in here, the royal cook has been sick"
    'living_room')
evil_queen = Room(
    "Evil Queen Location",
    "Well, you made it to the Evil Queen in her long dark purple gown, gook luck",
    None, None, "living_room", None, None, None, None, evil_queeen)
player = Player(ricos_food_truck)
# Controller
playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down', 'move']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    player.inventory = []
    if player.current_location.item is not None:
        try:
            print("There is a %s here." %
                  player.current_location.item.name.lower())
        except AttributeError:
            pass
    command = input(">_")
    if player.current_location.item is not None and command.lower() in [
            'pick up', 'grab', 'take'
    ]:
        player.inventory.append(player.current_location.item.name)
        print("Your player picked up the %s" %
              player.current_location.item.name.lower())
        print(player.inventory)
        player.current_location.item = None
    elif command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
    else:
        print("Command not found")
