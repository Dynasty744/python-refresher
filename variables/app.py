# Lessons from Programming with Mosh
# https://www.youtube.com/watch?v=kqtD5dpn9C8

# Primitives or Basic types in Python
# 1 number (int)
# 1.1 number (float)
# True/False boolean
# 'a' string

# VARIABLE
# no need to use var/let/const like JS, just declare and initialize
# if a variable is an empty box, then
# declare means to create an empty box
# initialize means to put something in that empty box
#
# patient_name = 'Dynasty 744'
# patient_age = '20'
# new_patient = True
# print('We are checking in ' + patient_name + ', the patient is at the age of ' + patient_age + ', and he is a new patient')

# INPUT
#
# name = input("What is your name? ")
# print("Hello " + name)

# TYPE CONVERSION
#
# birth_year = input("Enter your birth year: ")
# current_age = 2024 - int(birth_year) # conversion here
# print(current_age)

# ADDITION CALCULATOR
# can also type covert at input
#
# first_number = input("Gimme the first number: ")
# second_number = input("Now gimme the second number: ")
# sum = float(first_number) + float(second_number)
# print("Sum: " + str(sum))

# STRINGS
#
# course = 'Python for Beginners'
# print(course.upper())
# print(course.find('y')) # .find(y) will return the index of the first occurence of 'y'
# print(course.find('for'))
# print(course.replace('for', '4'))
# print('Python' in course) # True

# ARITHMETIC OPERATORS
#
# print( 10 / 3) # returns a float
# print( 10 // 3) # returns int
# print( 10 ** 3) # returns 10 to the power of 3
# x = 10
# x = x + 3 # x is now 13
# x += 3 # same as line 49, called augmented assignment operator

# COMPARISON OPERATORS
# these will produce boolean values from the expression
#
# >
# >=
# <=
# ==
# !=

# LOGICAL OPERATORS
#
# price = 25
# print(price > 10 and price < 30) # True
# print(price > 10 or price < 24) # True
# print(not price > 25) # True

# IF STATEMENTS
#
# temperature = 9
# if temperature > 30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif temperature > 20:
#     print("It's a nice day")
# elif temperature > 10:
#     print("It's a bit cold")
# else:
#     print("It's damn cold")
# print("Done")

# CONVERSION EXERCISE
# first, the program asks for my weight, let's say 170
# next it's asking if weight is in (K)g or (L)bs, lower or uppercase, doesn't matter, let's say 'l'
# then output with "Weight in Kg: 76.5"
# weight = float(input("What is your weight? "))
# unit = input("(K)g or (L)bs? ").lower()
# if unit == 'l':
#     print("Weight in Kg: " + str(weight * 0.45))
# elif unit == 'k':
#     print("Weight in Lbs: " + str(weight * 2.20462))
# else:
#     print("Invalid input. Please enter 'K' for Kg or 'L' for Lbs.")

# WHILE LOOPS
# repeat a block of code multiple times
#
# i = 1

# while i <= 5:
#     print(i * '*') # able to multiply a number by a string
#     i = i + 1

# LISTS
# is a complex type in Python
# 
# names = ["John", "Bob", "Mosh", "Sam", "Mary"]
# names[0] = 'Jon'
# print(names[-2])
# print(names[0:3]) # does not modify original list, but returns a new list
# print(names)

# LIST METHODS
#
# numbers = [1, 2, 3, 4, 5]
# numbers.append(6) # add to the end of the list
# numbers.insert(0, -1)
# numbers.remove(3)
# print(len(numbers)) # returns the number of elements in list
# print(1 in numbers)
# numbers.clear() # clear all values in list
# print(numbers)

# FOR LOOPS
# for loop would be a better implementation
# numbers = [1, 2, 3, 4, 5]
# for item in numbers: # item is a loop variable
#     print(item)

# i = 0 # item is a loop variable
# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1

# RANGE() FUNCTION
# use range to generate a sequence of numbers
#
# numbers = range(5, 10, 2)
# for number in range(5, 10, 2):
#     print(number)

# TUPLES
# kind of like lists, stores sequence of objects, but are immutable
# numbers = (1, 2, 3, 3)
# print(numbers.count(3))
# print(numbers.index(2))
# numbers[0] = 10