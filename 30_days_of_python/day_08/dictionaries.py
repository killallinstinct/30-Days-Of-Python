# Day 8: 30 days of python programming
# Exercises

# 1. Create an empty dictionary called dog
# dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'Blaire',
    'breed': 'Beagle mix',
    'legs': 4,
    'age': 13
}

# 3. Create a student dictionary and add first_name, last_name, gender, age, martial status, skills, country, city,
# address, as keys for the dictionary

student = {
    'first_name': 'Ryou',
    'last_name': 'Yamada',
    'gender': 'F',
    'age': '16',
    'is_married': False,
    'skills': ['bass guitar mastery', 'adaptability', 'resourcefulness', 'opportunism'],
    'address': {
        'street': 'Unknown',
        'city': 'Tokyo',
        'country': 'Japan',
    }
}
# 4. Get the length of the student dictionary
# print(len(student))     # 7

# 5. Get the value of skills and check the data type, it should be a list
# print(len(student['skills']))   # 4
# print(type(student['skills']))  # is list

# 6. Modify the skills values by adding one of two skills
# student['skills'].append('comedic timing')
# student['skills'].append('unpredictable charm')
# print(student['skills'])

# 7. Get the dictionary keys as a list
# keys = student.keys()
# print(keys)

# 8. Get the dictionary values as a list
# pairs = student.values()
# print(pairs)

# 9. Change the dictionary to a list of tuples using the items() method
# student.items()

# 10. Delete one of the items in the dictionary
# student.pop('address')
# print(student)

# 11. Delete one of the dictionaries
# dog.clear()
# print(dog)  # {}


# CONGRATS YOU DID IT AGAIN!!




