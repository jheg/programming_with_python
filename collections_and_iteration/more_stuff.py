# function chaining 

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def times(n1, n2):
    return n1 * n2

sum = add(40, 35)
print(sum)

difference = subtract(80, 20)
print(difference)

print(add(10,20))
print(subtract(100,21))

print(times(add(30,20), subtract(10,5)))

result = times(sum, difference)
print(result)


# Method chaining
tv_show = "Monty Python's Flying circus"
# tv_show = tv_show.upper()

# tv_show = tv_show.split()

tv_show = tv_show.upper().split()
print(tv_show)


letters = "abcdefghijklmnopqrstuvwxyz"

consonants = (letters.replace('a', '').
                      replace('e', '').
                      replace('i', '').
                      replace('o', '').
                      replace('u', ''))

print(consonants)

# Modules
print()
print('Modules')
import math
print(math.sqrt(36))        # 6.0
print(math.sqrt(2))         # 1.4142135623730951
print(math.pi)

from datetime import datetime as dt
print()
print('Modules - DateTime')
date = dt.strptime("July 16, 2022", "%B %d, %Y")
weekday_name = date.strftime('%A')
print(weekday_name)

print()
print('Function Definition order')

def top():
    bottom()

def bottom():
    print('You have reached the bottom')

top()

def foo():
    def bar():
        print('BAR')

    bar() # BAR

foo()
# bar() # NameError: name 'bar' is not defined

print()
print('The global and nonlocal Statements')
greeting = 'Salutations'

def well_howdy(name):
    greeting = "Howdy"
    print(f'{greeting}, {name}!')

well_howdy('Victoria')
print(greeting)
