import csv


with open("Sales Records(1).csv", 'r') as old_csv:
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
        if row[2] == "Fruits"

