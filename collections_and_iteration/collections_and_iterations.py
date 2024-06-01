# Sequences
# ranges, lists, tuples
# strings are text sequences but are not a collection 
from gettext import find


letters = ['a', 'b', 'c']
print(letters[0])   # a
print(letters[1])   # b
print(letters[2])   # c

# lists are heterogenous, they can contain a diverse range of objects
my_list = [
    'May',
    2.99,
    {None, True, False},
    [1, 2, 3],
]

# ranges are homogenous; they always contain integers

# strings are not objects as they contain characters which are strings of length 1

# sets
# Set contain unique elements or members
letters = {'a', 'b', 'c'}
letters.add('d')
print(letters)
# {'a', 'b', 'c', 'd'} (order may differ)

frozen_letters = frozenset(letters)
# frozen_letters.add('e')
# AttributeError: 'frozenset' object has no
# attribute 'add'

# Sets and frozen sets are heterogenous
my_set = {
    'May',
    2.99,
    (None, True, False),
    range(5),
}

# sets are not ordered even though python 
# may print them in order it is not guaranteed
numbers = {1,5,4,3,2}
print(numbers)
numbers = {1, 2, 37, 4, 5}
print(numbers)

# What are Maps?
# Dicts are mutable
# They consist of key value pairs
# They are unordered
# The keys must be unique, adding the duplicate will replace the existing 
d = {'a': 1, (1, 3): 3, 1: 'x'}
print(d)         # {'a': 1, (1, 3): 3, 1: 'x'}
print(d['a'])    # 1
print(d[(1, 3)]) # 3
print(d[1])      # 'x'

d['a'] = 'A'
print(d)        # {'a': 'A', (1, 3): 3, 1: 'x'}


d = {'a': 1, (1, 3): 3, 1: 'x'}

del d['a']      # Deletes key/value pair 'a': 1
print(d)        # {(1, 3): 3, 1: 'x'}

d['a'] = 42
print(d)        # {(1, 3): 3, 1: 'x', 'a': 42}

# Sequence Constructors
r = range(5, 12, 2)
print(list(r))            # [5, 7, 9, 11]

r = range(12, 8, -1)
print(list(r))            # [12, 11, 10, 9]

r = range(12, 5, -2)
print(list(r))            # [12, 10, 8, 6]

r = range(5, 5, 1)
print(list(r))           # []

r = range(5, 7, -1)
print(list(r))            # []

my_str = 'Python'

my_list = list(my_str)
print(my_list)  # ['P', 'y', 't', 'h', 'o', 'n']

my_tuple = tuple(my_list)
print(my_tuple) # ('P', 'y', 't', 'h', 'o', 'n')

my_set = set(my_tuple)
print(my_set)   # {'t', 'o', 'n', 'h', 'P', 'y'}

my_list = [5, 12, 2]
another_list = list(my_list)

print(my_list)                          # [5, 12, 2]
print(another_list)                     # [5, 12, 2]

print(my_list == another_list)          # True
print(my_list is another_list)          # False

# Exercises
# 1
people = ('Jason', 'Victoria', 'Charlie', 'Annie')
print(len(people))

#2
stuff = ('hello', 'world', 'bye', 'now')
mystuff = list(stuff)
mystuff[2] = 'Goodbye'
stuff = tuple(mystuff)
print(stuff)
print(type(stuff))

#3
# Lists and Tuples are similar in that both are heterogenous and are both sequence collections
# but they differ in that lists are mutable whilst tuples are not and lists use [] and tuples use ()

#4 
# Strings can be treated as sequences as they are order and the characters can be accessed with indexing

#5
# Set types are unordered collections, cannot be indexed and use {}  

#6
pi = 3.141592
str_pi = str(pi)
print(str_pi)
print(type(str_pi))

#7 
range(7)            # 0-6
range(1, 6)         # 1-5
range(3, 15, 4)     # 3, 7, 11
range(3, 8, -1)     # - 
range(8, 3, -1)     # 8-4

#8 
print(list(range(3, 17, 4)))

#9 
my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Are the lists assigned to my_list and another_list equal?                         YES
# Are the lists assigned to my_list and another_list the same object?               NO
# Are the nested lists at index 3 of my_list and another_list equal?                YES
# Are the nested lists at index 3 of my_list and another_list the same object?      YES
print(my_list[3] is another_list[3])
my_list[3][0] = 42
print(my_list)
print(another_list)
print(my_list[3] is another_list[3])

# Note using the list constructor creates a shallow copy which means 
# only top level elements are copied but nested elements are referenced 
# which means if you mutate one it will impact both lists. 
# You should create deep copies if you want to avoid this

#10 
# No as sets are unordered collections

#11
names_and_locations = {
    'Alice': 'USA',
    'Francois': 'Canada',
    'Inti': 'Peru',
    'Monika': 'Germany',
    'Sanyu': 'Uganda',
    'Yoshitaka': 'Japan',
}
def find_country(name):
    print(names_and_locations[name])

find_country('Monika')
