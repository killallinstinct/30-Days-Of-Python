# Day 11: 30 days of python programming
import math
import statistics


# Exercises
# Level 1

# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total


# print(add_two_numbers(2, 3))  # debug

# 2. Area of a circle is calculated as follows: area = pi * r * r.
# Write a function that calculates area_of_circle.
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


# print(area_of_circle(3))  # debug

# 3. Write a function called add_all_numbers which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_numbers(*nums):
    total = 0
    for num in nums:
        if num is type(int):
            total += num
        else:
            # print('yeah nice try buddy')
            pass
    return total


# print(add_all_numbers(2, 3, 4, 'c'))  # debug

# 4. Temperature in C can be converted to F using this formula: F = (C * 9/5) + 32.
# Write a function which converts C to F, convert_celsius_to_fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return f"32 in Celsius is {fahrenheit} in Fahrenheit"


# print(convert_celsius_to_fahrenheit(32))    # debug


# 5. Write a function called check_season,
# it takes a month parameter and returns the season: Autumn, Winter, Spring, or Summer.
def check_season(month):
    month = month.lower()
    if month in ['december' or 'january' or 'february']:
        return 'winter'
    elif month in ['march' or 'april' or 'may']:
        return 'spring'
    elif month in ['june' or 'july' or 'august']:
        return 'summer'
    elif month in ['september' or 'october' or 'november']:
        return 'autumn'
    else:
        return 'fail'


# debug usage
# month = input("Enter the month: ")
# print(f"The season is: {check_season(month)}")

# 6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(m, x, b):
    y = (m*x)+b
    return y

# debug
# print(calculate_slope(2,2,2))


# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0.
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):

    # calculate discriminant
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)

    elif discriminant == 0:
        root = -b / (2*a)

    else:   # complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return complex(real_part, imaginary_part), complex(real_part, -imaginary_part)


a, b, c = 1, -3, 3
solutions = solve_quadratic_eqn(a, b, c)
# print(f"Solutions: {solutions}")


# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for i in lst:
        print(i)


# debug
alphabet = ['a', 'b', 'c', 'd']
# print(alphabet)


# 9. Declare a function named reverse_list.
# It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
    return lst[::-1]


# print(f"Reversed list: {reverse_list(alphabet)}")


# 10. Declare a function named capitalize_list_items.
# It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(items):
    return [item.capitalize() for item in items]


# print(capitalize_list_items(alphabet))


# 11. Declare a function named add_item. It takes a list and an item parameters.
# It returns a list with the item added at the end.
def add_item(lst, item):
    lst.append(item)
    return lst


# print(add_item(alphabet, 'e'))


# 12. Declare a function named remove_item. It takes a list and an item parameters.
# It returns a list with the item removed from it.
def remove_item(lst, item):
    lst.remove(item)
    return lst


# print(remove_item(alphabet, 'a'))

# 13. Declare a function named sum_of_numbers.
# It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(number):
    if number < 0:
        return "Enter a non-negative number"
    return sum(range(number+1))


# print(sum_of_numbers(5))    # 15

# 14. Declare a function named sum_of_odds.
# It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(number):
    if number < 0:
        return "Enter a non-negative number"

    return sum(i for i in range(number+1) if i % 2 != 0)


# print(sum_of_odds(100)) # 2500

# 15. Declare a function named sum_of_even.
# It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_evens(number):
    if number < 0:
        return "Enter a non-negative number"

    return sum(i for i in range(number+1) if i % 2 == 0)


# print(sum_of_evens(100)) # 2550


# Level 2
# 1. Declare a function named evens_and_odds .
# It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(number):
    evens = 0
    odds = 0
    if number < 0:
        return "try again"
    else:
        for i in range(number+1):
            if i % 2 == 0:
                evens += 1
            elif i % 2 != 0:
                odds += 1

    return f"The number of evens are: {evens}\nThe number of odds are: {odds}"


# print(evens_and_odds(100))

# 2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number):
    if number < 0:
        return "try again, kid"

    elif number == 0 or number == 1:
        return 1

    result = 1
    for i in range(2, number+1):
        result *= i
    return f"The factorial is: {result}"


# print(factorial(10)) # 3628800


# 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(value):
    return not bool(value)


# debug center
"""print(is_empty([]))
print(is_empty(2))
print(is_empty(" "))
print(is_empty(""))"""


# 4. Write different functions which take lists.
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance,
# calculate_std (standard deviation).
def calculate_mean(lst):
    return sum(lst) / float(len(lst))


def calculate_median(lst):
    return statistics.median(lst)


def calculate_mode(lst):
    return max(lst, key=lst.count)


def calculate_range(lst):
    lst.sort()
    return lst[-1] - lst[0]


def calculate_variance(lst):
    return statistics.variance(lst)


def calculate_std(lst):
    return statistics.stdev(lst)


# Level 3
# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(number):
    if number <= 1: # 0 and 1 are not prime
        return False
    if number == 2: # 2 is the only even prime
        return True
    if number % 2 == 0: # eliminate other even numbers greater than 2
        return False

    # check for factors from 3 to the square root of the number
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False

    return True


# print(is_prime(3))


# 2. Write a functions which checks if all items are unique in the list.
def is_unique_list(lst):
    return len(lst) == len(set(lst))


# 3. Write a function which checks if all the items of the list are of the same data type.
def all_same_type(lst):
    if not lst: # empty list
        return True

    # get type of first item in list then compare to all other items in list
    first_type = type(lst[0])
    return all(type(i) is first_type for i in lst)


# 4. Write a function which check if provided variable is a valid python variable
def is_valid_variable(name):
    # check if the name is a valid python identifier and is not a keyword
    import keyword
    return name.isidentifier() and name not in keyword.kwlist


# 5. I'm not doing this again


# HOORAAAAAAYYIIPPPEEEE!!!








