# Day 7: 30 days of python programming

# Exercises: Level 1
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies
# print(len(it_companies))    # 7

# 2. Add 'Twitter' to it_companies
# it_companies.add('Twitter')
# print(it_companies)   # Debug

# 3. Insert multiple IT companies at once to the set it_companies
# it_companies.update(['Intel', 'Infosys', 'CISCO'])
# print(it_companies)   # Debug

# 4. Remove one of the companies from the set it_companies
# it_companies.pop()
# print(it_companies)   # Debug

# Exercises: Level 2
# 1. Join A and B
# C = A.union(B)
# print(C)

# 2. Find A intersection B
# print(A.intersection(B))

# 3. Is A subset of B
# print(A.issubset(B))    # True

# 4. Are A and B disjoint sets?
# print(A.isdisjoint(B))  # False

# 5. Join A with B and B with A
# C = A.union(B)
# D = B.union(A)
# print(C)
# print(D)

# 6. What is the symmetric difference between A and B
# print(A.symmetric_difference(B))    # {27, 28}

# 7. Delete the sets completely
# del A, B
# print(A)    # error
# print(B)    # error

# Exercises: Level 3
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# st_ages = set(age)
# print(len(st_ages))     # 5
# print(len(age))         # 8

# 2. Explain the difference between the following data types: string, list, tuple, and set
'''
Text is a string data type
A collection that which is ordered, modifiable and allows duplicate members is a list
A collection that which is ordered but not modifiable and allows duplicate members is a tuple
A collection that which is unordered, modifiable, and does not allow duplicate members but can add new items is a set
'''

# 3. "I am a teacher and I love to inspire and teach people." How many unique words have been used in the sentence?
# Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
unique_words = set(sentence.split())
unique_word_count = len(unique_words)
print(f"number of unique words: {unique_word_count}")   # number of unique words: 10

#   YIPPPEEEE!!!



