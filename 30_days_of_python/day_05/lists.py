from countries import countries
# Day 5: 30 days of python programming

# Exercises: Day 5
# Exercises: Level 1

# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
more_than_five = ['rice', 'corn', 'chicken', 'beans', 'pico', 'fajita vegetables']

# define middle of list

# Find the length of your list
# print(len(more_than_five))  # 6

# Get the first item, the middle item, and the last item of the list
'''first_item = more_than_five[0]
middle_index = int((len(more_than_five) - 1) / 2)   # list has an even number of items
middle_item = more_than_five[middle_index]
last_index = len(more_than_five) - 1
last_item = more_than_five[last_index]
print(first_item)
print(middle_item)
print(last_item)'''

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Kai', 24, 62, 'Single', '123 Nonexistence St']  # name, age, height in inches, is_single, address

# Declare a list variable named it_companies
# and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
# print(it_companies)

# Print the number of companies in the list
# print('Number of items in list:', len(it_companies))    # 7

# Print the first, middle and last company
"""first_item = it_companies[0]
middle_index = int(len(it_companies) / 2)
middle_item = it_companies[middle_index]
last_index = len(it_companies) - 1
last_item = it_companies[last_index]
print(first_item)   # Facebook
print(middle_item)  # Apple
print(last_item)    # Amazon"""

# Print the list after modifying one of the companies
# it_companies[0] = 'Meta'
# print(it_companies)

# Add an IT company to it_companies
# it_companies.append('Tencent')
# print(it_companies)

# Insert an IT company in the middle of the companies list
# middle_index = int(len(it_companies) / 2)
# it_companies.insert(middle_index, 'Alphabet Inc.')
# print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
# it_companies[0] = it_companies[0].upper()
# print(it_companies)

# Join the it_companies with a string '#;  '
# string = '#; '
# it_companies.extend(string)
# print(it_companies)

# Check if a certain company exists in the it_companies list.
# does_exist = 'Meta' in it_companies
# print(does_exist)   # False

# Sort the list using sort() method
# it_companies.sort()
# print(it_companies) # sorted alphabetically

# Reverse the list in descending order using reverse() method
# it_companies.sort(reverse=True)
# print(it_companies)

# Slice out the first 3 companies from the list
# print(it_companies[3:])

# Slice out the last 3 companies from the list
# print(it_companies[:-3])

# Slice out the middle IT company or companies from the list
# middle_item = int(len(it_companies) / 2)
# it_companies.pop(middle_item)
# print(it_companies)

# Remove the first IT company from the list
# del it_companies[0]
# print(it_companies)

# Remove the middle IT company or companies from the list
# del it_companies[middle_index]
# print(it_companies)

# Remove the last IT company from the list
# it_companies.pop()
# print(it_companies)

# Remove all IT companies from the list
# it_companies.clear()    # airs out the whole list
# print(it_companies)     # nothingness

# Destroy the IT companies list
# del it_companies  # deletes the whole list xD
# print(it_companies) # Error because list no longer exists

# Join the following lists:
'''front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack.
# Then insert Python and SQL after Redux.
full_stack = front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)'''

# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# constant
middle_index = int(len(ages) / 2)
min_age = ages[0]
max_age = ages[-1]

# Sort the list and find the min and max age easier
ages.sort()

# Add the min age and the max age again to the list
# ages.append(min_age)
# ages.append(max_age)
# ages.sort()


# Find the median age (one middle item or two middle items divided by two)
if len(ages) % 2 == 0:
    middle_1 = ages[middle_index - 1]
    middle_2 = ages[middle_index]
    median = int((middle_1 + middle_2) / 2)
    # print(median)

elif len(ages) % 2 == 1:
    pass
    # print(ages[middle_index])

# Find the average age (sum of all items divided by their number)
sum_of_ages = sum(ages)
average_of_ages = sum_of_ages / len(ages)
# print('Sum of ages:', sum_of_ages)  # 228
# print('Average age:', average_of_ages)  # 22.8

# Find the range of the ages (max minus min)
range_of_ages = ages[-1] - ages[0]
# print(range_of_ages)    # 7

# Compare the value of (min - average) and (max - average), use abs() method
# print(abs(min_age - average_of_ages) == abs(max_age - average_of_ages)) # False

# Exercises: Level 3(?)
# print(len(countries))   # 193

# constant
middle_index2 = len(countries) // 2  # 96
# print(countries[middle_index2])

# Find the middle country(ies) in the countries list
if len(countries) % 2 == 0:
    middle_1 = countries[middle_index2 - 1]
    middle_2 = countries[middle_index2]
    # print(middle_1, middle_2)

elif len(countries) % 2 == 1:
    print(countries[middle_index2])

# Divide the countries list into two equal lists if it is even; if not, add one more country for the first half.
split_countries1 = countries[:middle_index2 + 1]
split_countries2 = countries[middle_index2:]

# print(len(split_countries1), len(split_countries2))

# Unpack the first three countries and the rest as scandic countries.
specific_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *scandic = specific_countries
# print(scandic)
