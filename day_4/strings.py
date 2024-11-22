# Day 4: 30 Days of python programming

# Exercises - Day 4
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
a, b, c, d = 'Thirty', 'Days', 'Of', 'Python'
space = ' '
string = a + space + b + space + c + space + d
# print(string)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
e, f, g = 'Coding', 'For', 'All'
string2 = e + space + f + space + g
# print(string2)


# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print().
# print(company)

# Print the length of the company string using len() method and print().
# print(len(company))

# Change all the characters to uppercase letters using upper() method.
# print(company.upper())

# Change all the characters to lowercase letters using lower() method.
# print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
# print(company.capitalize())
# print(company.title())
# print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
# print(company[6:])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
# print(company.find('Coding'))

# Replace the word coding in the string 'Coding For All' to Python.
# print(company.replace('Coding', 'Python'))

# Split the string 'Coding For All' using space as the separator (split()).
# print(company.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
# companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
# print(companies.split(", "))

# What is the character at index 0 in the string Coding For All.
# print(company[0])     # C

# What is the last index of the string Coding For All.
# print(company[-1])    # l

# What character is at index 10 in "Coding For All" string.
# print(company[10])      # whitespace

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
'''
string3 = 'Python For Everyone'
output_string = string3[0]

for i in range(1, len(string3)):
    if string3[i - 1] == ' ':
        output_string += string3[i]

output_string = output_string.upper()

print(output_string)
'''
'''
# Create an acronym or an abbreviation for the name 'Coding For All'.
output_string = company[0]

for i in range(1, len(company)):
    if company[i - 1] == ' ':
        output_string += company[i]

output_string = output_string.upper()

print(output_string)
'''
# Use index to determine the position of the first occurrence of C in Coding For All.
# print(company.find('C'))

# Use index to determine the position of the first occurrence of F in Coding For All.
# print(company.find('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
# print(company.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
# sentence = 'You cannot end a sentence with because because because is a conjunction'
# print(sentence.find('because'))

# Use rindex to find the position of the last occurrence of the word because in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
# sentence = 'You cannot end a sentence with because because because is a conjunction'
# print(sentence.rindex('because'))

# Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
# sentence = 'You cannot end a sentence with because because because is a conjunction'
# print(sentence.replace('because', ''))

# Find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
# sentence = 'You cannot end a sentence with because because because is a conjunction'
# print(sentence.find('because'))

# Does 'Coding For All' start with a substring Coding?
# print(company.startswith('Coding'))

# Does 'Coding For All' end with a substring coding?
# print(company.endswith('coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
# wide_company = '   Coding For All      '
# print(company.strip(' '))

# Which one of the following variables return True when we use the method isidentifier():
#
#     30DaysOfPython
#     thirty_days_of_python
# challenge = '30DaysOfPython'
# print(challenge.isidentifier()) # False, starts with a number
# challenge = 'thirty_days_of_python'
# print(challenge.isidentifier()) # True

# The following list contains the names of some of python libraries:
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'].
# Join the list with a hash with space string.
# python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# print(' '.join(python_libraries))

# Use the new line escape sequence to separate the following sentences.
#
# I am enjoying this challenge.
# I just wonder what is next.
# print('I am enjoying this challenge.\nI just wonder what is next.')

# Use a tab escape sequence to write the following lines.
#
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
# print('Name \t\tAge \tCountry \tCity')
# print('Asabeneh \t250 \tFinland \tHelsinki')

# Use the string formatting method to display the following:
#
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
'''
radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area)
print(formatted_string)
'''
# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144

a = 8
b = 6
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# It's over
