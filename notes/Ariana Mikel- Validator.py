import csv
# Drop the last digit from the number. The last digit is what we want to check against
# Reverse the numbers
# Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
# Add all the numbers together
# The check digit (the last number of the card) is the amount that you would need to add to get a multiple of 10
# (Modulo 10)


def sixteen_digits(num: str):
    if (len(num)) == 16:
        if (len(num)) == 16:
            return True
        else:
            print("Not every number has 16 digits")
            return False
def divisible_by_2(number: int):
    if number % 2 == 0:
        return True
    return False

def valid_card_number(num: str):
    if not sixteen_digits(num):
        return False
    valid_card_number_list = list(num)
    valid_card_number_list.pop(15)
    for number in range

def reverse(string):
    print(string[::-1])


def multiply(num: str):
    num =