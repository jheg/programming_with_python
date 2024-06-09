seq = ('a','b','c')
print(seq[0])       # a 
print(seq[1])       # b 
print(seq[2])       # c 
# print(seq[3])       # IndexError; tuple index out of range 

last_index = len(seq) -1
print(seq[last_index])

# negative indexes
print(seq[-1])

# reassigning mutable sequences
seq = [1,2,3]
seq[0] = 0
print(seq)

# Slicing
seq = 'abcdefghi'
print(seq[3:7])         # defg
print(seq[-6:-2])       # defg    
print(seq[2:8:2])       # ceg
print(repr(seq[3:3]))   # ''
print(seq[3:3])         #
print(seq[:])           # abcdefghi
print(seq[::-1])        # ihgfedcba

seq = [[1,2],[3,4]]
seq_dup = seq[:]
print(seq[0] is seq_dup[0])     # True (Shallow copy rules)
print(seq is seq_dup)           # False (Shallow copy rules)

# dicts
my_dict = {
    'a': 'abc',
    37: 'def',
    (5, 6, 7): 'ghi',
    frozenset([1, 2]): 'jkl'
}

print(my_dict['a'])                 # abc
print(my_dict[37])                  # def
print(my_dict[(5, 6, 7)])           # ghi
print(my_dict[frozenset([1, 2])])   # jkl
# print(my_dict['nothing'])         # KeyError: 'nothing'
print(my_dict.get('nothing'))       # None
print(my_dict.get('nothing', 100))  # 100

my_dict['a'] = '123'
print(my_dict['a'])

from curses.ascii import isalpha
from pprint import pprint
my_dict = {
    'a': 'abc', 
    'b': 'def',
    'c': {
        'd': 'ghi',
        'e': 'jkl'
    }
}
print(my_dict)
pprint(my_dict)

my_dict = {
    'a': 'abc',
    'b': 'def',
    'c': {
        'd': 'ghi',
        'e': 'jkl',
        'f': {
            'g': 'mno',
            'h': 'pqr',
            'i': {
                'j': 'stu',
                'k': 'vwx',
                'l': 'yz'
            }
        }
    }
}

print("Using print:")
print(my_dict)

print("\nUsing pprint:")
pprint(my_dict)

my_dict['xyz'] = 'Hey there!'
pprint(my_dict)

# Common collection Operations
# Non-mutating operations
# Collection membership
seq = [4, 'abcdef', (True, False, None)]
print(4 in seq)                 # True
print(4 not in seq)             # False
print(True in seq)              # False
print(True in seq[2])           # True
print(5 not in seq)             # True

# min max members
my_set1 = {1, 4, -9, 16, -36, -63, -1}
my_set2 = {'1', '4', '-9', '16', '-36', '-63', '-1'}
print(min(my_set1), max(my_set1))       # -63 16
print(min(my_set2), max(my_set2))       # -1 4

# summation
numbers = (1, 1, 2, 3, 5, 8, 13, 21, 34)
print(sum(numbers))         # 88

# indices 
names = ['Karl', 'Grace', 'Clare', 'Victor', 
         'Antonia', 'Allison', 'Trevor']
print(names.index('Clare'))     # 2
# print(names.index('Clate'))     # ValueError: 'Clate' not in list

# count
numbers = [1, 3, 6, 5, 4, 10, 1, 5, 4, 4, 5, 4]
print(numbers.count(4))             # 4
print(numbers.count('Chris'))       # 0 
print(numbers.count(32))            # 0 

names = 'Karl Grace Victor Clare'
print(names.index('Karl'))

iterable1 = [1, 2, 3]
iterable2 = ('Kim', 'Leslie', 'Bertie')
iterable3 = [None, True, False]

zipped_iterables = zip(iterable1, iterable2, iterable3)
print(list(zipped_iterables))

result = zip(range(5, 10),    # length is 5
             range(1, 3),     # length is 2 (shortest)
             range(3, 7))     # length is 4
print(list(result)) # [(5, 1, 3), (6, 2, 4)]

result = zip(range(5, 10),    # length is 5
             range(1, 3),     # length is 2 (shortest)
             range(3, 7),     # length is 4
             strict=True)     
# print(list(result))           # ValueError argument 2 is horter than argument 1

# Operations on Dictionaries
people_phones = {
    'Chris': '01234567890',
    'John': '01234567891',
    'Clare': '01234567892',
}

print(people_phones.items())
print(people_phones.keys())
print(people_phones.values())

people_phones = {
    'Chris': '111-2222',
    'Pete':  '333-4444',
    'Clare': '555-6666',
}

keys = people_phones.keys()
values= people_phones.values()

print(keys)    # dict_keys(['Chris', 'Pete', 'Clare'])
print(values)
# dict_values(['111-2222', '333-4444', '555-6666'])

people_phones['Max'] = '123-4567'
people_phones['Pete'] = '345-6789'
del people_phones['Chris']

print(keys)    # dict_keys(['Pete', 'Clare', 'Max'])
print(values)
# dict_values(['345-6789', '555-6666', '123-4567'])

# Operations for Mutable Sequences
numbers = [1, 2]
print(numbers)

numbers.append(3)
print(numbers)

numbers.insert(1, 6)
print(numbers)

numbers.extend([5,6])
print(numbers)

numbers.remove(6)
print(numbers)

print(numbers.pop())
print(numbers)

numbers.clear()
print(numbers)

# Sorting Collections
numbers = [2, 4, 7, 1, 3, 4, 9, 8, 7]
names = ['Jason', 'Vic', 'Charlie', 'Annie']

print(sorted(numbers)) # does not mutate the list
print(sorted(names))

numbers.sort() # mutates the list
print(numbers)

words = ['abc', 'DEF', 'xyz', '123']
print(sorted(words))
# ['123', 'DEF', 'abc', 'xyz']

print(sorted(words, key=str.lower))
# ['123', 'abc', 'DEF', 'xyz']

numbers = ['1', '5', '100', '15', '534', '53']
numbers.sort()
print(numbers)   # ['1', '100', '15', '5', '53', '534']

numbers.sort(key=int)
print(numbers)   # ['1', '5', '15', '53', '100', '534']

names = ('Grace', 'Clare', 'Allison', 'Trevor')
reversed_names = reversed(names)
print(reversed_names)
print(tuple(reversed(names)))
print(names)

names = list(names)
print(names.reverse())
print(names)

my_dict = {'abc': 1, 'xyz': 23, 'pqr': 0, 'jkl': 5}
reversed_dict = reversed(my_dict)
print(reversed_dict)

print(list(reversed_dict))

# String Operations
print("what's up?".capitalize())        # What's up?
print('456ABC'.capitalize())            # 456abc
print("What's up?".swapcase())          # wHAT'S UP?
print('456abc'.swapcase().swapcase())   # 456abc 

# Character Classification
name = 'Jason'
print(name.isalpha())

'Hello'.isalpha()      # True
'Good-bye'.isalpha()   # False: `-` is not a letter
'Four score'.isalpha() # False: space is not a letter
''.isalpha()           # False

'12340'.isdigit()      # True
'123.4'.isdigit()      # False: `.` is not a digit
'-1234'.isdigit()      # False: `-` is not a digit
''.isdigit()           # False

text = input('What is your name? ').strip()
print(repr(text))

text = ' \t  abc def    \n\r'
print(repr(text.strip('abc'))) # ' \t  abc def    \n\r'

text = 'aaabaacccabxyzabccba'
print(text.strip('a'))         # baacccabxyzabccb
print(text.strip('ab'))        # cccabxyzabcc
print(text.strip('ba'))        # cccabxyzabcc
print(text.strip('abc'))       # xyz
print(text.strip('bc'))        # aaabaacccabxyzabccba

print(repr(text.strip('abcxyz'))) # ''

print(list('Jason'))

text = '''
You were lucky to have a room. We used to have to
live in a corridor.
Oh we used to dream of livin' in a corridor!
Woulda' been a palace to us. We used to live in an
old water tank on a rubbish tip. We got woken up
every morning by having a load of rotting fish
dumped all over us.
'''

pprint(text.strip().splitlines())
# Pretty printed for clarity
[
    "You were lucky to have a room. We used to have to",
    "live in a corridor.",
    "Oh we used to dream of livin' in a corridor!",
    "Woulda' been a palace to us. We used to live in an",
    "old water tank on a rubbish tip. We got woken up",
    "every morning by having a load of rotting fish",
    "dumped all over us."
]

words = ['You', 'were', 'lucky']
print(''.join(words))
print(' '.join(words))
print(','.join(words))
print('\n '.join(words))

school = 'launch school'

print(school.find(' '))       # 6
print(school.find('l'))       # 0
print(school.find('h'))       # 5
print(school.find('hoo'))     # 9
print(school.find('x'))       # -1
print(school.find('N'))       # -1

print(school.rfind(' '))      # 6
print(school.rfind('l'))      # 12
print(school.rfind('h'))      # 9
print(school.rfind('hoo'))    # 9
print(school.rfind('oh'))     # -1
print(school.rfind('N'))      # -1

deck = [
    { 'suit': 'Clubs', 'value': '2' },
    { 'suit': 'Clubs', 'value': '3' },
    { 'suit': 'Clubs', 'value': '4' },
    { 'suit': 'Spades', 'value': 'Queen' },
    { 'suit': 'Spades', 'value': 'King' },
    { 'suit': 'Spades', 'value': 'Ace' },
]

print(f"The 50th casd in the deck is the {deck[4]['value']} of {deck[4]['suit']}")

# Exercises
#1
numbers = range(0, 25, 3)
print(numbers[6])

# 2
launch_school = 'Launch School'
print(launch_school[4:10])

# 6
print('abc-def'.isalpha())          
print('abc_def'.isalpha())
print('abc def'.isalpha())
print('abc def'.isalpha() and
      'abc def'.isspace())
print('abc def'.isalpha() or
      'abc def'.isspace())
print('abcdef'.isalpha())
print('31415'.isdigit())
print('-31415'.isdigit())
print('31_415'.isdigit())
print('3.1415'.isdigit())
print(''.isspace())

# 7 Write Python code to replace all the : characters in the string below with +
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

my_list = info.split(':')
new_list = '+'.join(my_list)
print(my_list)
print(new_list)

full_name = ['Jason' 'Lee' 'Hegarty']
fullname = ''.join(full_name)
print(fullname)

print(info)
infos = info.replace(':', '+')
print(infos)