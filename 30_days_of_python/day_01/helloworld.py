"""
# User input for student score
score = int(input('Enter student score: '))

# Conditionals to grade the score within 0-100 parameter
if score > 100:  # Makes sure is less than or equal to 100
    print('scores are 0-100')
elif 100 >= score > 89:     # if 100 >= score and score > 89
    print('A')
elif 89 >= score > 69:
    print('B')
elif 69 >= score > 59:
    print('C')
elif 59 >= score > 49:
    print('D')
elif 0 <= score < 49:       # if score < 49
    print('F')
elif score < 0:             # Makes sure score is greater than 0 (non-negative)
    print('scores are 0-100')
"""

"""
# Lists to contain months in seasonal periods
winter = ['december', 'january', 'february']
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']
autumn = ['september', 'october', 'november']

# User input to get the current month
month = input('What current month is it: ')
month = month.lower()

# Compare user input to contents in lists
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

"""
# Given list of fruits
fruits = ['banana', 'orange', 'mango', 'lemon']

# Get user input of fruit to add to list
fruit = input('What fruit would you like to add to the list: ')
fruit = fruit.lower()

if fruit in fruits:     # If fruit is in list, disregard
    print('Fruit is already in the list, I fear')
else:                   # Else append fruit to list then display modified list
    fruits.append(fruit)
    print(fruits)
"""

person = \
    {
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
"""
mid_index1 = len(person['skills']) // 2 - 1
mid_index2 = len(person['skills']) // 2
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    print(person['skills'][2])

# Check if the person dictionary has skills key, if so, check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print(person['skills'])
"""

"""
# If a person skills has only JavaScript and React, print('He is a front end developer'),
if person['skills'] == ['JavaScript', 'React'] or ['React', 'JavaScript']:
    print('He is a front end developer')

# if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
elif 'Node' and 'Python' and 'MongoDB' in person['skills']:

    # if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
    if 'React' and 'Node' and 'MongoDB' in person['skills']:
        print('He is a fullstack developer')
    else:
        print('He is a backend developer')

# else print('unknown title') - for more accurate results more conditions can be nested!
else:
    print('unknown title')
"""

"""
# If the person is married and if he lives in Finland, print the information in the following format:
# 'Asabeneh Yetayeh lives in Finland. He is married.'
if person['is_marred'] == True and person['country'] == 'Finland':
    print(person['first_name'] + ' ' + person['last_name'] + ' lives in ' + person['country'] + '. He is married')
else:
    print('Ya done smucked up KID!')
"""

# EXERCISE LEVEL 1 + 2
print(type(10))                                 # int
print(type(9.8))                                # float
print(type(3.14))                               # float
print(type(4-4j))                               # complex
print(type(['Asabeneh', 'Python', 'Finland']))  # list
print(type('Kai'))                              # str
print(type('Of The Cross'))                     # str
print(type('America'))                          # str

# EXERCISE LEVEL 3
num = 2                                         # int
floater = 2.5                                   # float
complexer = 2 - 69j                             # complex
strings = 'string'                              # string
is_this_a_boolean = True                        # boolean
lovers = ['Lucario', 'Azumarill']               # list
more_lovers = ('69', '420')                     # tuple
even_MORE_lovers = {'Azarath', 'Mithras'}       # set
dictionary = {'friend': 'no'}                   # dictionary

dist1 = abs(2 - 3)
dist2 = abs(8 - 10)

# print(dist1, dist2, sep=", ")
