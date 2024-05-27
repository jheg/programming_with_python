def my_multiply(num1, num2):
    print(f'{num1} * {num2} = {float(num1) * float(num2)}')

first_number = input('Enter the first number: ')
second_number = input('Enter the second number: ')

my_multiply(first_number, second_number)

def multiply(left, right):
    return left * right

def get_number(prompt):
    entry = input(prompt)
    return float(entry)

first_number = get_number('Enter the first number: ')
second_number = get_number('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')