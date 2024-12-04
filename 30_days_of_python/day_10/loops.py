from countries import countries
from countries_data import countries_data
from collections import Counter

# Day 10: 30 days of python programming

# Exercises: Level 1

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
"""
for iterator in range(11):
    print(iterator)

count = 0
while count < 11:
    print(count)
    count = count + 1
"""

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
"""
for number in range(10, -1, -1):
    print(number)

number = 10
while number >= 0:
    print(number)
    number -= 1
"""

# 3. Write a loop that makes seven calls to print(), so we get on the output [half a] triangle:
"""
for number in range(1, 8):
    print('#' * number)'''
"""
# 4. Use nested loops to create [a 8x8 banner of #'s]
"""
for i in range(9):              # for 8 rows
    for j in range(9):          # for 8 cols
        print('#', end=' ')     # prints '#' and stays on the same line
    print()                     # move to next line after cols condition

"""
# 5. Print out a multiplication table with both operands starting at 0 and ending at 10:
"""
number = 0
while number < 11:
    result = number**2
    print(f"{number} X {number} = {result}")
    number += 1
"""

# 6. Iterate through the list, ['Python','Numpy','Pandas','Django','Flask'] using a for loop and print out the items:
"""
programming_languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in programming_languages:
    print(language)
"""

# 7. Use for a loop to iterate from 0 to 100 and print only even numbers
"""
for even_numbers in range(101):
    if even_numbers % 2 == 0:
        print(even_numbers)
"""
# 8. Use for loop to iterate from 0 to 100 and only print odd numbers
"""
for odd_numbers in range(101):
    if odd_numbers % 2 != 0:
        print(odd_numbers)
"""

# Exercises: Level 2

# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
"""
loop_sum = 0
for i in range(101):
    loop_sum += i
print(f'The sum of all numbers is {loop_sum}')
"""

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
"""
even_sum = 0
odd_sum = 0

for even_numbers in range(101):
    if even_numbers % 2 == 0:
        even_sum += even_numbers

for odd_numbers in range(101):
    if odd_numbers % 2 != 0:
        odd_sum += odd_numbers

print(f'The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.')
"""

# Exercises: Level 3
# (These were incredibly hard and not fun to do with the knowledge I had beforehand.)
# (And I hope the developer of this challenge updates this section in the future.)

# 1. Go to the data folder and use the countries.py file.
# Loop through the countries and extract all the countries
# containing the word 'land'.
"""
 for country in countries:
    if "land" in country:
        print(country)
"""

# 2. This is a fruit list,
# ['banana', 'orange', 'mango', 'lemon']
# reverse the order using loop.
"""
fruit_list = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(fruit_list) - 1, -1, -1):
    print(fruit_list[i])
"""

# 3. Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
"""
all_languages = []
for country in countries_data:
    all_languages = all_languages + country["languages"]
unique_languages = set(all_languages)
print(f"The total number of languages: {len(unique_languages)}")
"""
# Find the 10 most spoken languages from the data

"""
# collect all languages into a list
all_languages = []
for country in countries_data:
    all_languages.extend(country["languages"])

# counter the occurrences of each language
language_counts = Counter(all_languages)

# sort the languages by frequency and get top 10
most_spoken_languages = language_counts.most_common(10)

# print
for language, count in most_spoken_languages:
    print(f"{language}: {count}")
"""

# Find the 10 most populated countries in the world
"""
# sort the countries by population in descending order
most_populated_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]

# print
for country in most_populated_countries:
    print(f"{country['name']}: {country['population']}")
"""

# I do not feel any joy from completing these exercises
