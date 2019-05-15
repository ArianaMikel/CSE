import csv


with open("Sales Records (1).csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    fruits = 0
    clothes = 0
    meat = 0
    beverages = 0
    office_supplies = 0
    cosmetics = 0
    personal_care = 0
    household = 0
    baby_food = 0
    vegetables = 0
    snacks = 0
    cereal = 0
    print("Processing...")
    for row in reader:
        if row[2] == "Fruits":
            profits = float(row[13])
            for i in row[13]:
                fruits += profits
        elif row[2] == "Clothes":
            profits = float(row[13])
            for i in row[13]:
                clothes += profits
        elif row[2] == "Meat":
            profits = float(row[13])
            for i in row[13]:
                meat += profits
        elif row[2] == "Beverages":
            profits = float(row[13])
            for i in row[13]:
                beverages += profits
        elif row[2] == "Office Supplies":
            profits = float(row[13])
            for i in row[13]:
                office_supplies += profits
        elif row[2] == "Cosmetics":
            profits = float(row[13])
            for i in row[13]:
                cosmetics += profits
        elif row[2] == "Personal Care":
            profits = float(row[13])
            for i in row[13]:
                personal_care += profits
        elif row[2] == "Household":
            profits = float(row[13])
            for i in row[13]:
                household += profits
        elif row[2] == "Baby Food":
            profits = float(row[13])
            for i in row[13]:
                baby_food += profits
        elif row[2] == "Vegetables":
            profits = float(row[13])
            for i in row[13]:
                vegetables += profits
        elif row[2] == "Snacks":
            profits = float(row[13])
            for i in row[13]:
                snacks += profits
        elif row[2] == "Cereal":
            profits = float(row[13])
            for i in row[13]:
                cereal += profits

the_profits = [fruits, clothes, meat, beverages, office_supplies, cosmetics, personal_care, household,
               baby_food, vegetables, snacks, cereal]

print("The profit for fruits is %d" % fruits)
print("The profit for clothes is %d" % clothes)
print("The profit for meat is %d" % meat)
print("The profit for beverages is %d" % beverages)
print("The profit for office supplies is %d" % office_supplies)
print("The profit for cosmetics is %d" % cosmetics)
print("The profit for personal care is %d" % personal_care)
print("The profit for household is %d" % household)
print("The profit for baby food is %d" % baby_food)
print("The profit for vegetables is %d" % vegetables)
print("The profit for snacks is %d" % snacks)
print("The profit for cereal is %d" % cereal)


if max(the_profits) == fruits:
    print("Fruits are the most profitable")
if max(the_profits) == clothes:
    print("Clothes are the most profitable")
if max(the_profits) == meat:
    print("Meat is the most profitable")
if max(the_profits) == beverages:
    print("Beverages are the most profitable")
if max(the_profits) == office_supplies:
    print("Office supplies are the most profitable")
if max(the_profits) == cosmetics:
    print("Cosmetics are the most profitable")
if max(the_profits) == personal_care:
    print("Personal Care is the most profitable")
if max(the_profits) == household:
    print("Household items are the most profitable")
if max(the_profits) == baby_food:
    print("Baby Food is the most profitable")
if max(the_profits) == vegetables:
    print("Vegetable is the most profitable")
if max(the_profits) == snacks:
    print("Snacks are the most profitable")
if max(the_profits) == cereal:
    print("Cereal is the most profitable")
