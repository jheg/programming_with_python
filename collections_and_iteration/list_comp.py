# a transformative list comprehension
from audioop import mul


squares = [number * number for number in range(5)]
print(squares)

# same outcome with a regular loop
squares = []
for number in range(5):
    square = number * number
    squares.append(square)

print(squares)

# a selection list comprehension
multiples_of_6 = [number for number in range(20) if number % 6 == 0]
print(multiples_of_6)

# a combined selection and transformation clist comprehension
even_squares = [number * number for number in range(10) if number % 2 == 0]
print(even_squares)

# iterating over dicts 
cats_colours = {
    'Tess': 'brown',
    'Leo': 'orange',
    'Fluffy': 'gray',
    'Ben': 'black',
    'Kat': 'orange',
}

names = [name.upper() for name in cats_colours]
name_values = [value for value in cats_colours.values()]
name_pairs = [pair for pair in cats_colours.items()]
print(names)
print(name_values)
print(name_pairs)

# orange only
orange_cats = [name.upper() for name in cats_colours if cats_colours[name] == 'orange']
print(orange_cats)

names = [name.upper() for name in cats_colours 
         if cats_colours[name] == 'orange'
         if name[0] == 'L']

print(names)