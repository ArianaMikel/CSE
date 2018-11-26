# Creating Lists
'''
colors = ["blue", "turquoise", "pink", "orange", "black","red", "green", "purple", "violet", "black", "brown","grey" ] # USE SQUARE BRACKETS
print(colors)
print(colors[1])
print(colors[0])

# Length of the list
print("There are %d things in the list." % len(colors))

# Changing Elements in a list
colors[1] = "green"
print(colors)

# Looping through lists
for item in colors:
    print(item)

1. Make a list with 7 items
2. change the 3rd thing in the list
3. print the item
4. print the full list
'''

new_list = ["work", "school", "home", "supermarket", "restaurant", "beach", "prison"]
new_list[2] = "desert"
print(new_list)
print("The last thing in the list is %s" % new_list[len(new_list)-1])

# Slicing a list
print(new_list[1:3])
print(new_list[1:4])
print(new_list[1:])
print(new_list[:6])
