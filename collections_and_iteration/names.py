names = ['Jason', 'Victoria', 'Charlie', 'Annie', 'Pixie']

# while loops
upper_names = []
index = 0

while index < len(names):
    upper_name = names[index].upper()
    upper_names.append(upper_name)
    index += 1

print(upper_names)

# for loops
upper_names_for = []

for name in names: 
    upper_name = name.upper()
    upper_names_for.append(upper_name)

print(upper_names_for)

for char in 'Launch School':
    print(char)

for word in 'Launch School'.split():
    print(word)

my_set = {1000, 2000, 3000, 4000, 5000}
for member in my_set:
    print(member)
    # The order my be different to above as it comes from a set

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

for pair in my_dict.items():
    print(pair)

for key, value in my_dict.items():
    print(f'Key: {key} Value: {value}')

upper_name_cont = []
for name in names:
    if name == 'Pixie':
        continue

    upper_name = name.upper()
    upper_name_cont.append(upper_name)

print(upper_name_cont)