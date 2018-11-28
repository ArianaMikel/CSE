import random
number = random.randint(1, 10)
guesses = 5

while guesses > 0:
    num = int(input("Guess what number I'm thinking of between 1 and 10"))
    if num < number:
        print("Guess a higher number")
        guesses = guesses - 1
    elif num > number:
        print("Guess a lower number")
        guesses = guesses - 1
    elif num == number:
        print("Correct!")
        guesses = 0
