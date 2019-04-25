class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Hammer(Weapon):
    def __init__(self):
        super(Hammer, self).__init__("Hammer", 30)


class GlassBottle(Weapon):
    def __init__(self):
        super(GlassBottle, self).__init__("Glass Bottle", 20)


class Knife(Weapon):
    def __init__(self):
        super(Knife, self).__init__("Knife", 35)


class Machete(Weapon):
    def __init__(self):
        super(Machete, self).__init__("Machete", 60)


class Chair(Item):
    def __init__(self):
        super(Chair, self).__init__("Chair")


class Table(Weapon):
    def __init__(self):
        super(Table, self).__init__("Table", 20)


class FryingPan(Weapon):
    def __init__(self):
        super(FryingPan, self).__init__("Frying Pan", 24)


class Branch(Weapon):
    def __init__(self):
        super(Branch, self).__init__("Branch", 15)


class Pistol(Weapon):
    def __init__(self):
        super(Pistol, self).__init__("Pistol", 80)


class Scepter(Weapon):
    def __init__(self):
        super(Scepter, self).__init__("Scepter", 99)


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


class Food(Item):                               # Cookie
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
