# Day 3: 30 Days of python programming
"""
# Declare your age as integer variable
# Declare your height as a float variable
# Declare a variable that store(s) a complex number
age = 24
height = 62     # in inches
complexity = 6 + 9j

# Script that prompts user to enter base and height of a triangle to calculate its area (area = 0.5 * b * h)
base_of_triangle = int(input('Enter base: '))
height_of_triangle = int(input('Enter height: '))
print('The area of the triangle is', int(0.5 * base_of_triangle * height_of_triangle))

# Script that prompts user to input sides a, b, and c of a triangle to calculate its perimeter
# (perimeter = a + b + c)
side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
print('The perimeter of the triangle is', int(side_a + side_b + side_c))

# Script that prompts user to input length and width of a rectangle to calculate area and perimeter
# area = length * width and perimeter = 2 * (length + width)
length_of_rect = int(input('Enter length: '))
width_of_rect = int(input('Enter width: '))
print('The area of the rectangle is', int(length_of_rect * width_of_rect))
print('The perimeter of the rectangle is', int(2 * (length_of_rect + width_of_rect)))

# Script that prompts user to input radius of circle to calculate its area and circumference where pi = 3.14
# area of circle = pi * radius ** 2 and circumference = 2 * pi * radius
pi = 3.14
radius_of_circle = int(input('Enter radius: '))
print('The area of the circle is approx.', pi * radius_of_circle ** 2)
print('The circumference of the circle is approx.', 2 * pi * radius_of_circle)

# Identify the slope, x-intercept, and y-intercept of the given equation y = 2x - 2
equation = 'y = 2x - 2'
slope = 2
y_intercept = -2
x_intercept = 1     # equation(1) = 0
print('Given equation:', equation)
print('Slope:', slope)
print('Y-intercept:', y_intercept)
print('X-intercept:', x_intercept)

# Script that finds the slope and Euclidean distance between the two points (2, 2) and (6, 10)
# slope is m = (y2 - y1)/(x2 - x1)
point1 = '(2, 2)'
point2 = '(6, 10)'
x1 = 2
y1 = 2
x2 = 6
y2 = 10
print('Given points:', point1, ',', point2)
print('The slope is', int((y2 - y1)/(x2 - x1)))
print('Their Euclidean distance is', int(((y1 - x1) ** 2) + (y2 - x2) ** 2))

# Compare the last two slopes found with each other
print(slope != int((y2 - y1)/(x2 - x1)))

# Calculate y
# Try to figure out what x-value that makes y = 0 (p.s. it's -3)
x = 1
y = x**2 + 6*x + 9
print(y)

# Compare length of 'python' and 'dragon' and make a falsy comparison statement
print(not len('python') == len('dragon'))

# Use 'and' operator to check if 'on' is in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')    # True

# Use 'in' operator to check if the word is found in the string
print('jargon' in 'I hope this course is not full of jargon')   # True

# There is no 'on' in both 'dragon' and 'python'
print('on' not in 'dragon' and 'on' not in 'python')    # False

# Find length of the text 'python' and convert the value to a float and convert it to a string
length_of_python = len('python')
print(length_of_python)         # 6
print(float(length_of_python))  # 6.0
print(str(length_of_python))    # '6'

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = float(input('Enter an integer: '))
if int(num) % 2 == 0:
    print('The integer is even')
else:
    print('The integer is odd')

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print(7 // 3 == 2.7)    # False

# Check if type of '10' is equal to type of 10
print(type('10') is type(10))   # False

# Check if int('9.8') is equal to 10
print(int(9.8) == 10)   # False

# Writ(e) a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input('Enter hours: '))
rate = float(input('Enter rate per hour: '))
print('Your weekly earning is $', (hours * rate))

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live.
# Assume a person can live hundred years
seconds_in_a_year = 31536000
years_lived = int(input('Enter number of years you have lived: '))  # Assume 100
print('You have lived for', years_lived * seconds_in_a_year, 'seconds.')

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
for i in range(1, 6):
    print(i, ' ', i**0, ' ', i**1, ' ', i**2, ' ', i**3)    # First try btw
"""