import csv


def validate(num: str):
    if not all_16_digits(num):
        return False
    if divisible_by_2(num) and divisible_by_3(num):
        return True
    return False


def divisible_by_3(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False


def divisible_by_2(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False


def all_16_digits(num: str):
    if len(num) == 16:
        return True
    else:
        print("NOT EVERY NUMBER IS 16 DIGITS")
# with open("Book1.csv", 'r') as old_csv:
#     with open("myNewFile.csv", 'w', newline='') as new_csv:
#         print("Writing file...")
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         for row in reader:
#             old_number = int(row[0])
#             new_number = old_number + 1
#             row[0] = new_number
#             writer.writerow(row)
# old_number = int(row[0]) + 1
# print(old_number)
#         with open("Book1.csv", 'r') as old_csv:
#             with open("myNewFile.csv", 'w', newline='') as new_csv:
#                 print("Writing file...")
#                 reader = csv.reader(old_csv)
#                 writer = csv.writer(new_csv)
#                 for row in reader:
#                     old_number = row[0]
#                     first_num = int(old_number[0])
#                     if first_num % 2 == 0:
#                         writer.writerow(row)
#                     # print(int(old_number) + 1)
#                     # print(old_number)
# print("OK")


def reverse(string):
    print(string[::-1])

    reverse("Hello World")

with open("Book1.csv", 'r') as old_csv:
    with open("myNewFile.csv", 'w', newline='') as new_csv:
        print("Writing file...")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            # print(int(old_number) + 1)
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)
print("Done")


def valid_credit_card_number(num: str):

    print(valid_credit_card_number("7820959846382680"))
