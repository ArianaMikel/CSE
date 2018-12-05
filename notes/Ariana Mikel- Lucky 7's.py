import random
cash = 15
rounds = 0
highest = 15
while cash > 0:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 + dice2 == 7:
        cash += 4
        print("You got a seven, you are not a failure")
        rounds = rounds - 1
        if dice1 + dice2 > 7 or dice1 + dice2 < 7:
            print("Oof, you did not get 7, you FAILED")
            cash -= 1
            print("You got")
            print(dice1 and dice2)
            print("-+")
            rounds += 1
            if cash > highest:
                highest = cash

print("You played")
print(rounds)
print("You had the most money when you had")
print(highest)
print("dollars")
