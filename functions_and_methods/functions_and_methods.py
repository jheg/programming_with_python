# Calling Functions
from operator import is_

def hello():
    print('Hello')
    return True

hello()             # invoking function; ignore return value
print(hello())      # using return value in a 'print' call

print(print())      # None

print('Hello', 'Goodbye', 'Farewell')


print(              # spreading args over several lines
    'hello',
    'good-bye',
    'farewell',
    'adios',
    'ciao',
    'auf wiedersehen',
)

# Built-in Functions
# min and max
print(min(-10, 5, 12, 0, -20))          # -20
print(max(-10, 5, 12, 0, -20))          # 12

print(min('over', 'the', 'moon'))       # moon
print(max('over', 'the', 'moon'))       # the

# print(max(-10, '5', '12', '0', -20))  # TypeError: '>' not supported between instances
                                        # of 'str' and 'int'

my_tuple = ('i', 'tawt', 'i', 'taw', 'a', 
            'puddy', 'cat')
print(min(my_tuple))                     # a
print(max(my_tuple))                     # tawt

# ord and chr
print(ord('a'))         # 97
print(ord('A'))         # 65
print(ord('='))         # 61
print(ord('~'))         # 126

print(ord('a'))         # 97
print(ord('b'))         # 98
print(ord('c'))         # 99
print(ord('d'))         # 100

print(chr(97))          # a
print(chr(65))          # A
print(chr(61))          # =
print(chr(126))         # ~

# any and all
collection1 = [False, False, False]     # List
collection2 = (False, True, False)      # Tuple
collection3 = {True, True, True}        # Set

print(any(collection1))                 # False
print(any(collection2))                 # True
print(any(collection3))                 # True
print(any([]))                          # False

print(all(collection1))                 # False
print(all(collection2))                 # False
print(all(collection3))                 # True
print(all([]))                          # True

# Notice that any returns False for an empty collection since none of the elements are truthy. 
# However, all returns True for the same collection since none of the elements are falsy 
# (all of the elements are thus truthy).

numbers = [2, 5, 8, 10, 13]
print([number % 2 == 0 for number in numbers]) # comprehension
# True False True True False

print(any([number % 2 == 0 for number in numbers]))     # True
print(all([number % 2 == 0 for number in numbers]))     # False

numbers = [5 ,13]
print(any([number % 2 == 0 for number in numbers]))     # False
print(all([number % 2 == 0 for number in numbers]))     # False

numbers = [2, 8, 10]
print(any([number % 2 == 0 for number in numbers]))     # True
print(all([number % 2 == 0 for number in numbers]))     # True


# Functions for the REPL
print(id(numbers))

# Scope
greeting = 'Salutations'

def well_howdy(who):
    greeting = 'Howdy'
    print(f'{greeting}, {who}')

well_howdy('Jason')
# print(greeting)       # NameError: name 'greeting' is not defined
print(greeting)

def scope_test():
    if True:
        foo = 'Hello'
    else: 
        bar = 'Goodbye'
    
    print(foo)
    print(bar)

# scope_test()

# IMPORTANT
# parameters and arguments are not the same thing. 
# parameters are placeholders for the objects passsed to the function 
# and arguments are the objects passed in to the function during invocation

# Return values 
# predicates are functions that always return a Boolean value

def is_digit(char):
    if char >= '0' and char <= '9':
        print(char)
        return True

    print(char)
    return False

print(is_digit('a'))
print(is_digit('5'))
print(is_digit('10'))

# Functions versus Methods
# method invocation syntax
my_str = 'abc-123-def'
print(my_str.upper())

# Mutating the caller
odd_numbers = [1, 3, 5, 7, 9]
odd_numbers.pop()
print(odd_numbers)

def add_new_number(my_list):
    my_list.append(9)

numbers = [1, 2, 3, 4, 5]
add_new_number(numbers)
print(numbers)

# Returning a new object
def add_new_number(my_list):
    return my_list + [9]

numbers = [1, 2, 3, 4, 5]
new_numbers = add_new_number(numbers)
print(new_numbers) # [1, 2, 3, 4, 5, 9]
print(numbers)     # [1, 2, 3, 4, 5]