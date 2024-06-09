# Chapter: Using Collections 2nd run through 
# 09/06/2024 
# Was struggling on exercises a little so re reading this chapter. 
name = "Jason"
print(name[0])
# name[0] = "P"         # TypeError 'str' does not support item assignment
print(name[1:4])        # Slicing
print(name[::-1])       # Slicing

seq = ('a', 'b', 'c')   # This is a tuple ()
print(seq[0])           # a (1st element)
print(seq[1])           # b (2nd element)
print(seq[2])           # c (3rd element)
# print(seq[3])         # IndexError: tuple index out of range

seq = [0,1,2,3,4,5,6,7,8,9,10]
print(seq[::-1])

# Exercises 
# 1 Write Python code to print the seventh number of range(0, 25, 3).
numbers = list(range(0, 25, 3))
print(numbers[6])

# 2 
# Use slicing to write Python code to print 
# a 6-character substring of 'Launch School' that begins with the first c.
my_text = 'Launch School'
print(my_text[4:10])

# 3
# Write Python code to create a new tuple from (1, 2, 3, 4, 5). 
# The new tuple should be in reverse order from the original. It should also exclude the first and last 
# members of the original. The result should be the tuple (4, 3, 2).
numbers = (1, 2, 3, 4, 5)
new_tuple = numbers[3:0:-1]
print(new_tuple)

# 4 
# Part 1: Write some code to print Bark by accessing the element associated with the key Dog.
# Part 2: Write some code to print None when you try to print the value associated with the non-existent key, Lizard.
# Part 3: Write some code to print <silence> when you try to print the value associated with the non-existent key, Lizard.
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}
print(pets['Dog'])

if 'Lizard' in pets:
    print(pets['Lizard'])
else:
    print('<silence>')

print(pets.get('Lizard'))
print(pets.get('Lizard', '<silence>'))

# 5 Which of the following values can't be used as a key in a dict object, and why?
'cat'                               # OK
(3, 1, 4, 1, 5, 9, 2)               # OK
['a', 'b']                          # Not OK as lists are mutable and mutable objects are not hashable
{'a': 1, 'b': 2}                    # Not OK as dicts are mutable and mutable objects are not hashable
range(5)                            # OK
{1, 4, 9, 16, 25}                   # Not OK as set are mutable and mutable objects are not hashable
3                                   # OK
0.0                                 # OK
frozenset({1, 4, 9, 16, 25})        # OK

# 6 What will the following code print?
print('abc-def'.isalpha())          # false
print('abc_def'.isalpha())          # false
print('abc def'.isalpha())          # false
print('abc def'.isalpha() and
      'abc def'.isspace())          # false
print('abc def'.isalpha() or
      'abc def'.isspace())          # false
print('abcdef'.isalpha())           # true
print('31415'.isdigit())            # true
print('-31415'.isdigit())           # false 
print('31_415'.isdigit())           # false
print('3.1415'.isdigit())           # false
print(''.isspace())                 # false

# 7 Write Python code to replace all the : characters in the string below with +.
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
my_list = info.split(':')
new_info = '+'.join(my_list)
print(new_info)

# 9 
stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]
stuff[1][3] = 606
print(stuff)

# 10 
cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])

# 11
print('johnson' in 'Joe Johnson')           # false
print('sen' not in 'Joe Johnson')           # true
print('Joe J' in 'Joe Johnson')             # true
print(5 in range(5))                        # false
print(5 in range(6))                        # true
print(5 not in range(5, 10))                # false    
print(0 in range(10, 0, -1))                # false
print(4 in {6, 5, 4, 3, 2, 1})              # true    
print({1, 2, 3} in {1, 2, 3})               # false
print({3, 2} in {1, frozenset({2, 3})})     # true

# 12
numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

def check_for_3(numbers):
    if 3 in numbers:
        return True
    else: 
        return False

print('Exercise 12')
print(check_for_3(numbers1))
print(check_for_3(numbers2))
print(check_for_3(numbers3))
print(check_for_3(numbers4))
print(check_for_3(numbers5))

# 13 
cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats)           # True
print('Butter' in cats)                 # False
print('Butter' in cats[3])              # True
print('cheddar' in cats)                # False

# 14
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

# Write some code that combines the sequences into a list of tuples. 
# Each tuple should contain one member of each sequence. Print the 
# final result so you can see all the values, which should look like this:
[('a', 'Alpha', None, 10),
 ('b', 'Bravo', True, 20),
 ('c', 'Charlie', False, 30)]

list_of_tuples = zip(my_str, my_list, my_tuple, my_range)
print(list(list_of_tuples))