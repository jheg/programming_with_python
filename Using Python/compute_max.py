max = '0'
for number in ['10', '2', '34', '6', '25']:
    if number > max:
        max = number
print('Max value is: ',max)

# converted strings to integers to fix comparison
max = '0'
for number in ['10', '2', '34', '6', '25']:
    if int(number) > int(max):
        max = number
print('Max value is: ', max)