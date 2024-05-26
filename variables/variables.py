answer = 41
print(answer)       # 41

answer = 42
print(answer)       # 42

# naming conventions
# Use lowercase, numbers & underscores
# start with a letter
# Only use ASCII character set

# Class names
# Use PascalCase (Sometimes called CamelCase)
# Can contain upper and lowercase letters and numbers
# Capitalize7EachWord

# This is valid python and will create two variables and assign each arg respectively 
first,last = ['Mary', 'Wonder']
# first,last = ['Mary', 'Wonder', 'John'] # Error: Too many values to unpack, expected 2

print(first)
print(last)

forename = 'Clare'      # initialization (also called assignment)
forename = 'Victor'     # reassignment

# How Initialization and Reassignment Work
foo = 'abcdefghi'
print(foo)
foo = 'Hello' 
print(foo)

# Creating constants
# Use SCREAMING_SNAKE_CASE for constant naming
# Since constants should be unchanging, you should never reassign a constant.
# Constants aren't constant in Python
# Python does not support true constants
# Changing a constant's is poor practice and may make you unpopular at work! 
PINING_FOR = 'fjords'   # initialization


# Expressions and reassignment
foo = 42            # foo is 42
foo = foo - 2       # foo is now 40
foo = foo * 3       # foo is now 120
foo = foo + 5       # foo is now 125
foo = foo // 25     # foo is now 5
foo = foo / 2       # foo is now 2.5
foo = foo**3        # foo is now 15.625
print(foo)          # prints 15.625

# Augmented Assignment or Assignment Operators
foo = 42            # foo is 42
foo -= 2            # foo is now 40
foo *= 3            # foo is now 120
foo += 5            # foo is now 125
foo //= 25          # foo is now 5
foo /= 2            # foo is now 2.5
foo **= 3           # foo is now 15.625
print(foo)          # prints 15.625

# works with other types too
bar = 'xyz'          # bar is 'xyz'
bar += 'abc'         # bar is now 'xyzabc'
bar *= 2             # bar is now 'xyzabcxyzabc'
print(bar)           # prints xyzabcxyzabc

bar = [1, 2, 3]     # bar is [1, 2, 3]
bar += [4, 5]       # + with lists appends
                    # bar is now [1, 2, 3, 4, 5]
print(bar)          # prints [1, 2, 3, 4, 5]

bar = {1, 2, 3}     # bar is {1, 2, 3}
bar |= {2, 3, 4, 5} # | performs set union
                    # bar is now {1, 2, 3, 4, 5}
bar -= {2, 4}       # - performs set difference
                    # bar is now {1, 3, 5}
print(bar)          # prints {1, 3, 5}

# Note augmented assignment is a statement, not an expression. Thus, you cannot use aa as a function argument or return value
def foo(bar):
    print(bar)

a = 3
# foo(a *= 2)
#       ^^
# SyntaxError: invalid syntax

def foo():
    a = 3
#    return a *= 2
#             ^^
# SyntaxError: invalid syntax


# Reassignment vs. Mutation
"""Reassignment results in the variable pointing to a new object, 
whereas mutation alters the current object at the same memory location.

One subtle but important distinction is the difference between reassigning a 
variable and reassigning an element in a list, dict, or other mutable collection. 
Reassigning an element of a mutable collection doesn't reassign the variable; it mutates the collection.
"""
num = 3                 # assignment (initialization)
my_list = [1, 2, 3]     # assignment (initialization)
my_dict = {             # assignment (initialization)
    'a': 1,
    'b': 2,
}

num = 42                # Reassignment
my_list[1] = 42         # Reassignment of an element,
                        # my_list is mutated!
my_dict['b'] = 3        # Reassignment of a dict pair
                        # my_dict is mutated!

# You can still reassign the variables
my_list = (2, 3, 4)     # Reassignment
my_dict = {'x': 0}      # Reassignment

# Exercises
# 1 Variables
index = 1               # idiomatic
CatName = 'Tom'         # non-idiomatic, Class names use that naming convention
lazy_dog = 'John'       # idiomatic
quick_Fox = 'Sly'       # non-idiomatic, should be all lowercase
# 1stCharacter = 'a'      # illegal, should not start with a numeric
operand2 = 3            # idiomatic
BIG_NUMBER = 1000       # non-idiomatic, reserve theis for constants
π = 3.14                # non-idiomatic, ASCII characters only

# 2 Functions (same naming convention rules as variables)
# index                 # idiomatic
# CatName               # non-idiomatic
# lazy_dog              # idiomatic
# quick_Fox             # non-idiomatic
# 1stCharacter          # illegal
# operand2              # idiomatic
# BIG_NUMBER            # non-idiomatic
# π                     # non-idiomatic

# 3 CONSTANTS
index = 1               # non-idiomatic
CatName = 'Tom'         # non-idiomatic
snake_case = 'Jack'     # non-idiomatic
LAZY_DOG3 = 'John'      # idiomatic
# 1ST = 'a'             # illegal
operand2 = 3            # non-idiomatic
BIG_NUMBER = 1000       # idiomatic
π = 3.14                # non-idiomatic

# 4 Class names 
# index                 # non-idiomatic
# CatName               # idiomatic
# Lazy_Dog              # non-idiomatic
# 1ST                   # illegal
# operand2              # non-idiomatic
# BigNumber3            # idiomatic
# πi                    # non-idiomatic

# 5 see greeter.py
# 6 see age.py
# 7 
NAME = 'Victor'
print('Good Morning, ' + NAME)      # Good Morning, Victor.
print('Good Afternoon, ' + NAME)    # Good Afternoon, Victor.
print('Good Evening, ' + NAME)      # Good Evening, Victor.

NAME = 'Nina'
print('Good Morning, ' + NAME)      # Good Morning, Nina.
print('Good Afternoon, ' + NAME)    # Good Afternoon, Nina.
print('Good Evening, ' + NAME)      # Good Evening, Nina.

# The above will work just as any variable will work as constants aren't constant in python.

# 8 and 9 see balance.py
# 10 Reassign or Mutate
# assumes obj already has a value of 42. 
obj = 'ABcd'                # Reassignment
obj.upper()                 # Neither
obj = obj.lower()           # Reassignment
print(len(obj))             # Neither
obj = list(obj)             # Reassignment
obj.pop()                   # Mutation
obj[2] = 'X'                # Mutation
obj.sort()                  # Mutation
set(obj)                    # Mutation
obj = tuple(obj)            # Reassignment