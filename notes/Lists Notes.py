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


new_list = ["work", "school", "home", "supermarket", "restaurant", "beach", "prison"]
new_list[2] = "desert"
print(new_list)
print("The last thing in the list is %s" % new_list[len(new_list)-1])

# Slicing a list
print(new_list[1:3])
print(new_list[1:4])
print(new_list[1:])
print(new_list[:6])
'''



food_list = ["pizza", "enchiladas", "popcorn", "chicken", "cupcake", "cake", "cookies", "rice","noodles", "meatball",
             "clam chowder", "hamburger","chicken wings","salad", "french fries","salmon", "alfredo","garlic bread",
             "shrimp", "carne asada", "chili", "bread"]
print(len(food_list))

# Adding stuff to a list
food_list.append("bacon")
food_list.append("eggs")
# Notice that everything is object.method(parameters)
print(food_list)
food_list.insert(1, "eggo waffles")
print(food_list)

# Removing things from a list
food_list.remove("salad")
print(food_list)

'''
ari_list = ["pretzels", "pizza", "pie"]
print(ari_list)
ari_list.append("pecan")
print(ari_list)
ari_list.remove("pretzels")
print(ari_list)

# Tuples
brands = ("apple", "samsung", "HTC") # Noctice the parentheses, this is a tuple it cannot be changed, 
#it is immutable, not a list
'''

# Also removing stuff from a LIST
print(food_list)
food_list.pop(0)
print(food_list)


# Find the index of an item
print(food_list.index("chicken"))

# Changing things into a list, extremely handy para hangman
string1 = "turquoise"
list1 = list(string1)
print(list1)

# Turn a list into a string
print("".join(list1))

for i in range (len(list1)):  # i goes through all indicies
    if list1[i] == "u":   # if we find a U
        list.pop(i)   # remove the i-th index
        list.insert(i, "*")   # Put a * there instead
'''
for character in list1:
    is character == "u":
    #   replace with a *
    current_index = list1.index(character)
    list1.pop(current_index)
    list1.insert(current_index, "*")
'''
