# 1 
# counter never changes therefore always is less than 5

# 2 
# Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter. 
# The updated code should use a for loop to display the future ages.
# age = int(input('How old are you? '))
# print(f'You are {age} years old.')
# print(f'In 10 years, you will be {age + 10} years old.')
# print(f'In 20 years, you will be {age + 20} years old.')
# print(f'In 30 years, you will be {age + 30} years old.')
# print(f'In 40 years, you will be {age + 40} years old.')

age = int(input('How old are you? '))
years = [10, 20, 30, 40]
print(f'You are {age} years old.')

for year in years:
    print(f'In {year} years, you will be {age + year} years old.')

# solution without need for an array.
for future in range(10, 50, 10):
    print(f'In {future} years, you will be {age + future} years old.')

# 3 
# Use a while loop to print the numbers in my_list, one number per line. 
# Then, do the same with a for loop.
my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

for num in my_list:
    print(num)

# 4
# Use a while loop to print all numbers in my_list with even values, one number per line. 
# Then, print the odd numbers using a ' for' loop.
my_list = [6, 3, 0, 11, 20, 4, 17]
index = 0
print()
print('while loop')
while index < len(my_list):
    number = my_list[index]
    if number % 2 == 0:
        print(number)
    index += 1

print()
print('for loop')
for number in my_list:
    if number % 2 != 0:
        print(number)
    
# 5 
# Print all of the even numbers in the following list of nested lists. 
# Don't use any while loops.
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

print()
print('Question 5')
for list in my_list:
    for number in list:
        if number % 2 == 0:
            print(number)

# 6 
# Let's try another variation on the even/odd-numbers theme.

# We'll return to the simpler one-dimensional version of my_list. 
# In this problem, you should write code that creates a new list with one element for each number in my_list. 
# If the original number is an even, then the corresponding element in the new list should contain 
# the string 'even'; otherwise, the element should contain 'odd'.

print()
print('Question 6')
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]
new_list = []
for number in my_list:
    if number % 2 == 0: 
        new_list.append('even')
    else:
        new_list.append('odd')

print(new_list)

print()
print('ternary expression')
new_list_2 = ['even' if num % 2 == 0 else 'odd' for num in my_list]
print(new_list_2)

print()
print('Using a helper function')
def odd_or_even(number):
        return 'even' if number % 2 == 0 else 'odd'

new_list_3 = [odd_or_even(number) for number in my_list]
print(new_list_3)

# 7 
# Write a find_integers function that returns a list of all the integers from my_tuple:

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
def find_integers(tuple):
    my_list = []
    for element in tuple:
        if type(element) is int:
            my_list.append(element)
    return my_list

def find_integers_2(tuple):
    return [element for element in tuple if type(element) is int]

integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]

integers_2 = find_integers_2(my_tuple)
print()
print('Solution')
print(integers_2)

# 8 
# Write a comprehension that creates a dict object whose keys are strings and 
# whose values are the length of the corresponding key. 
# Only keys with odd lengths should be in the dict. 
# Use the set given by my_set as the source of strings.

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

my_dict = { key: len(key) for key in my_set if len(key) % 2 != 0 }
print()
print('Question 8')
print(my_dict)

# 9 
# Write a function that computes and returns the factorial of a number by using a for or while loop. 
# The factorial of a positive integer n, signified by n!, 
# is defined as the product of all integers between 1 and n, inclusive:
# n!	Expansion	        Result
# 1!	1	                1       total = 1
# 2!	1 * 2	            2       total = total(1) * 2 
# 3!	1 * 2 * 3	        6       total = total(2) * 3 ((( (1*2) + ((1*2) * 3)   ))
# 4!	1 * 2 * 3 * 4	    24      total = total(6) * 4
# 5!	1 * 2 * 3 * 4 * 5	120

def calculate_factorial(n):
    result = 1
    while n > 0:
        result *= n             
        n -= 1 

    print(result) 


def factorial(n):
    result = 1
    for num in range(n, 0, -1):
        result *= num
    
    print(result)



print()
print('Question 9')
print()
print('1 * 1')
calculate_factorial(1)
factorial(1)
print()
print()
print()
print('1 * 1 * 2')
calculate_factorial(2)
factorial(2)
print()
print()
print()
print('1 * 1 * 2 * 3')
calculate_factorial(3)
factorial(3)
print()
print()
print()
print('1 * 1 * 2 * 3 * 4')
calculate_factorial(4)
factorial(4)
print()
print()
calculate_factorial(5)
calculate_factorial(6)
calculate_factorial(7)
calculate_factorial(8)
calculate_factorial(25)

# 10 
# The following code uses the randrange function from Python's random library to obtain and print a random integer within a given range. 
# Using a while loop, it keeps running until it finds a random number that matches the last number in the range. 
# Refactor the code so it doesn't require two different invocations of randrange.

# see randrange.py 

# 11 
# Challenging Problem: Don't feel bad if you struggle with this problem or can't solve it. The problem is not easy. 
# It is designed to demonstrate why we prefer to use for loops when we can, 
# and a big part of that problem is messy code that is difficult to write and understand. 
# See how far you can get, but don't spend much time struggling.

# Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

index = len(my_list) - 1

while index >= 0: 
    nested_index = len(my_list[index]) -1 
    while nested_index >= 0:
        number = my_list[index][nested_index]
        if number % 2 == 0:
            print(number) 
        nested_index -= 1
    index -= 1



