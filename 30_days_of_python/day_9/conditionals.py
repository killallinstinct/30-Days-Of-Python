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
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print("a is greater than b.")
elif a < b:
    print("a is smaller than b.")
else:
    print("a is equal to b.")









