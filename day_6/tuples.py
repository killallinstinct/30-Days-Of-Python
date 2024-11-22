# Day 6: 30 days of python programming

# Exercises: Level 1
# 1. Create an empty tuple
empty_tuple = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('brandon', 'everest')
sisters = ('charlie', 'diane')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# 4. How many siblings do you have?
number_of_siblings = len(siblings)
# print(number_of_siblings) # Debug

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family members
parents = ('marianna', 'miguel')
family_members = siblings + parents
# print(family_members) # Debug

# Exercises: Level 2
# 1. Unpack siblings and parents from family members
siblings = family_members[0:4]
parents = family_members[4:]
# print(siblings)   # Debug
# print(parents)    # Debug

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called
# food_stuff_tp.
fruits = ('apple', 'banana', 'mango')
vegetables = ('broccoli', 'spinach', 'potato')
animal_products = ('milk', 'chicken', 'eggs')

food_stuff_tp = fruits + vegetables + animal_products
# print(food_stuff_tp)  # Debug

# 3. Change the about food_stuff_tp to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_item = food_stuff_lt[len(food_stuff_lt)//2]
# print(middle_item)    # Debug

# 5. Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[0:3]
last_three = food_stuff_lt[-3:]
# print(first_three)    # Debug
# print(last_three)     # Debug

# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp   # bye bye :(

# 7. Check if an item exists in the tuple:
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
# print('Estonia' in nordic_countries)  # Debug

# Check if 'Iceland' is a nordic country
# print('Iceland' in nordic_countries)  # Debug

# YOU DID IT!!!
