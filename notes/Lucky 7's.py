import random
cash = 15
rounds = 0
while cash > 0
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 + dice2 == 7:
        cash += 4
        rounds = rounds - 1
        if dice1