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

list_num = list(number)
for index in range(len(list_num)):
    list_num[index] = int(list_num[index])
    