"""Prompts the user for a name and outputs
a personalized greeting. 
"""
print("What's your name?")
name = input()

print(f'Good Morning, {name}!')

# You can also enter the prompt to the input()
name = input("What's your name? ")
print(f'Good Morning, {name}!')

# Alternatively we can have input out a newline instead of a space
name = input("What's your name?\n")
print(f'Good Afternnon, {name}!')

