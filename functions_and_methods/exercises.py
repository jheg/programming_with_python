# 1
def set_foo():
    foo = 'bar'

set_foo()
# print(foo)          # errors as foo is not defined. 

# 2
foo = 'bar'

def set_foo():
    foo = 'qux'

# set_foo()
# print(foo)          # 'bar'

# 3 see multiply.py 
# 4
# 5
def scream(words):
    return words + '!!!!'

scream('Yipeee')    # Returns 'Yipeee!!!!' but prints nothing

# 6 
def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')    # Returns True but prints nothing as print after return

# 7 Errors expected 2 arguments got 1
# answer
# TypeError: foo() missing 1 required positional
# argument: 'qux'

# 8 Error: expected 2 got 3

# 9 prints 42 3.141592 2.718

# 10 prints 42 3.141592 2

# 11 prints 42 3 2

# 12 Error first not defined
# Answer: 
# TypeError: foo() missing 1 required positional
# argument: 'first'

# 13 Error: all subsequent default values must also have a default value 

# 14
def multiply(left, right):                                  # multiply, left, right
    return left * right                                     

def get_num(prompt):                                        # get_num, prompt 
    return float(input(prompt))

first_number = get_num('Enter the first number: ')          # first_number
second_number = get_num('Enter the second number: ')        # second_number
product = multiply(first_number, second_number)             # product
print(f'{first_number} * {second_number} = {product}')

# Also float, input, print


# 15 
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# multiply      GLOBAL
# left          LOCAL
# right         LOCAL
# get_num       GLOBAL
# prompt        LOCAL
# float         BUILT-IN
# input         BUILT-IN
# first_number  GLOBAL
# second_number GLOBAL
# product       GLOBAL
# print         BUILT-IN


# 16
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Function names on lines 1, 4, 5, 7, 8, 9 & 10 (multiply, get_num, float, input, print)
# parameters on lines 1, 4

# 17
def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

# Function names:       say
# Method names          upper(), lower()
# Built-in functions    print, input, max

# 18
def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]           
numbers_3 = [0, 3, 6]
numbers_4 = []

remainders_3(numbers_1) # 3, 6
remainders_3(numbers_2) # 
remainders_3(numbers_3) # 3, 6
remainders_3(numbers_4) # 



# 19
def remainders_5(numbers):
    return [number % 5 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

print(all(remainders_5(numbers_1)))     # False
print(all(remainders_5(numbers_2)))     # True
print(all(remainders_5(numbers_3)))     # False
print(all(remainders_5(numbers_4)))     # True