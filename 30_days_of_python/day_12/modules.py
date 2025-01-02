# main file
from mymodule import generate_full_name as fullname, sum_two_nums as total
from math import *
import random
import string

# print(fullname('Alan', 'Fuentes'))

# print(total(1, 9))

# Exercises: Level 1


# 1. Write a function which generates a six digit/character random_user_id.
def generate_random_user_id():
    # returns random int between 100000 and 999999
    return random.randint(100000, 999999)


# print(generate_random_user_id())

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters
# but it takes two inputs using input(). One of the inputs is the number of characters
# and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    # pool of characters
    alphabet = string.ascii_lowercase + string.digits

    # take input to determine number of characters
    num_of_characters = int(input("How many number of characters (1-6): "))

    # take input to determine the number of IDS to be generated
    num_of_gens = int(input("How many IDs to gen: "))

    # generate the IDs
    ids = []
    for i in range(num_of_gens):
        random_id = ''.join(random.choices(alphabet, k=num_of_characters))
        ids.append(random_id)

    # print the generated IDs
    for user_id in ids:
        print(user_id)


# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    print(f'rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})')


# Exercises: Level 2

# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array
# (six hexadecimal numbers written after #.
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f.
# Check the task 6 for output examples).
def list_of_hexa_colors(num_colors):
    # generate list of hexa colors
    colors = []
    for i in range(num_colors):
        hexa_color = "#" + ''.join(random.choices('0123456789abcdef', k=6))
        colors.append(hexa_color)
    return colors


# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num_rgb):
    # generate list of rgb colors
    rgb_colors = []
    for i in range(num_rgb):
        rgb_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        rgb_colors.append(rgb_color)
    return rgb_colors


# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(arg1, num_of_colors):
    # generate list for colors
    colors = []

    # for hexa colors
    if arg1 == 'hexa':
        for i in range(num_of_colors):
            hexa_color = "#" + ''.join(random.choices('0123456789abcdef', k=6))
            colors.append(hexa_color)
        return colors   # returns as a list

    # for rgb colors
    elif arg1 == 'rgb':
        for i in range(num_of_colors):
            rgb_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            colors.append(f'rgb{rgb_color}')
        return colors   # returns as a list


# example usage
print(f'3 hex colors: {generate_colors("hexa", 3)}')
print(f'3 rgb colors: {generate_colors("rgb", 3)}')

# Exercises: Level 3

# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    random.shuffle(lst)
    return lst


# example usage
print(f'The list [1, 2, 3] is now shuffled into {shuffle_list([1, 2, 3])}')

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_random_numbers():
    # gen pool for numbers
    return random.sample(range(10), 7)  # choose 7 unique numbers from range 0-9


# example usage
print(f'Array of unique numbers: {unique_random_numbers()}')


# You are going far. Keep going!
# You have just completed day 12 challenges and you are 12 steps a head in to your way to greatness.
# Now do some exercises for your brain and muscles.





