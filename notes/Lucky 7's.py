import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
while dice1 + dice2 == 7:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
