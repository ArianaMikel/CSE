print("Hello World")
# Hello World


cars = 5
driving = True

print("I have %d cars" % cars)
print("I have " + str(cars) + " cars")

question_1 = input("How old are you?")
print(question_1 + "? Don't lie to me")

color = ["blue", "orange", "green", "purple","brown"]
color.append("black")

print(color)
color.pop(0)

print(color)
print(color[2])

print(len(color))

'''
print(string.ascii_letters)                # import string
print(string.digits)
print(string.punctuation)


while guesses > 0:
    num = int(input("Guess what number I'm thinking of between 1 and 10"))
    if num < number:
        print("Guess a higher number")
        guesses = guesses -1
    elif num > number:
        print("Guess a lower number")
        guesses = guesses -1
    elif num == number:
        print("Correct!")
        guesses = 0
'''


# while guesses > 0 and int(word_length) > 0:
   # if guesses = 0:
for i in range(word_length):
    output.append("_ ")