# 1 
def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

# CHRIS 

# 2
# Use the sqrt function from the math library to write some code that outputs the square root of 37. 
# Try to write the code in three different ways.
# import math
# print(math.sqrt(37))

# import math as m
# print(m.sqrt(37))

from math import sqrt
print(sqrt(37))
