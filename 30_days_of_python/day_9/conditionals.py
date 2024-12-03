# Day 9: 30 days of python programming

# Exercises: Level 1
# 1. Get user input using input("Enter your age: ").
# If the user is 18 or older, give feedback: You are old enough to drive.
# If below 18 give feedback to wait for the missing amount of years.
"""
minimum_age_to_drive = 18
age = int(input(f"Enter your age: "))
remaining_years = minimum_age_to_drive - age

if age >= minimum_age_to_drive:
    print("You are old enough to drive.")

elif age < minimum_age_to_drive:
    print(f"You'll need to wait", remaining_years, f"more year(s) until you can drive legally.")
"""

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”)
# to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age,
# 'years' for bigger differences, and a custom text if my_age = your_age.
"""my_age = 24
your_age = int(input("Enter your age: "))

if my_age > your_age and my_age - your_age == 1:
    print("I'm older than you by 1 year.")

elif my_age > your_age and my_age - your_age > 1:
    print(f"I'm older than you by", my_age - your_age, f"years.")

elif my_age < your_age and your_age - my_age == 1:
    print("You're older than me by 1 year")

elif my_age < your_age and your_age - my_age > 1:
    print(f"You're older than me by", your_age - my_age, f"years.")

elif my_age == your_age:
    print("What a coincidence, we're the same age.")
"""

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b
# if a is less than b return a is smaller than b, else a is equal to b.
'''a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print("a is greater than b.")
elif a < b:
    print("a is smaller than b.")
else:
    print("a is equal to b.")
'''
# Exercises: Level 2
# 1. Write a code which gives grade to students according to theirs scores:
'''class_grade = int(input("Enter the student's current grade: "))

if 90 <= class_grade <= 100:
    print("their grade is an A")

elif 70 <= class_grade <= 89:
    print("their grade is a B")

elif 60 <= class_grade <= 69:
    print("their grade is a C")

elif 50 <= class_grade <= 59:
    print("their grade is a D")

elif 0 <= class_grade <= 49:
    print("their grade is an F")

else:
    print("erm grades are in range from 0 - 100")
'''
# 2. Check if the season is Autumn, Winter, Spring, or Summer.
# If the user input is: September, October or November, the season is Autumn.
# December, January or February, the season is Winter.
# March, April or May, the season is Spring June, July or August, the season is Summer
"""
winter = ['december', 'january', 'february']
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
autumn = ['september', 'october', 'november']


month = input('What current month is it: ')
month = month.lower()


if month in winter:     # december, january or february
    print('The current season is winter')
    
elif month in spring:   # march, april or may
    print('The current season is spring')
    
elif month in summer:   # june, july or august
    print('The current season is summer')
    
elif month in autumn:   # september, october or november
    print('The current season is autumn')
    
else:                   # Error catch
    print('Not a month. Maybe check your spelling?')
"""

# 3. The following list contains some fruits:
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print('That fruit already exist in the list')
"""
# Given list of fruits
fruits = ['banana', 'orange', 'mango', 'lemon']


fruit = input('What fruit would you like to add to the list: ')
fruit = fruit.lower()

if fruit in fruits:     # If fruit is in list, disregard
    print('Fruit is already in the list, I fear')
    
else:                   # Else append fruit to list then display modified list
    fruits.append(fruit)
    print(fruits)
"""

# Exercises: Level 3
# 1. Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# Check if the person dictionary has skills key,
# if so print out the middle skill in the skills list.
'''if 'skills' in person:
    print(person['skills'][len(person['skills'])//2])'''

# Check if the person dictionary has skills key,
# if so check if the person has 'Python' skill and print out the result.
'''if 'skills' in person and 'Python' in person['skills']:
    print(person['skills'])
'''

# If a person skills has only JavaScript and React, print('He is a front end developer'),
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
# else print('unknown title') - for more accurate results more conditions can be nested!
if person['skills'] == ['JavaScript', 'React']:
    print('He is a front end developer')

elif 'Node' and 'Python' and 'MongoDB' in person['skills']:
    if 'React' and 'Node' and 'MongoDB' in person['skills']:
        print('He is a fullstack developer')

    else:
        print('He is a backend developer')

else:
    print('unknown title')

# If the person is married and if he lives in Finland,
# print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.
if person['is_marred'] is True and person['country'] == 'Finland':
    print('Asabeneh Yetayeh lives in Finland. He is married.')

elif person['is_marred'] is not True and person['country'] == 'Finland':
    print('Asabeneh Yetayeh lives in Finland. He is not married.')

elif person['is_marred'] is not True and person['country'] != 'Finland':
    print('Asabeneh Yetayeh does not live in Finland. He is not married.')

else:
    print('How did this even happen?')
