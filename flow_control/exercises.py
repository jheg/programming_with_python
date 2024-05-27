# 1
False or (True and False)       # False
True or (1 + 2)                 # True
(1 + 2) or True                 # 3
True and (1 + 2)                # 3
False and (1 + 2)               # False
(1 + 2) and True                # True
(32 * 4) >= 129                 # False
False != (not True)             # False
True == 4                       # False
False == (847 == '847')         # True

# 2
def even_or_odd(num):
    if num % 2 == 0:
        print('even')
    else: 
        print('odd')

even_or_odd(1)      # odd
even_or_odd(12)     # even
even_or_odd(113)    # odd

# 3
def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')     # Product2
bar_code_scanner(142)       # Product not found! > 142 not a str

# 4
# return ('bar' if foo() else qux())
# if foo():
#     return 'bar'
# else:
#     return qux()

# 5
def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])       # Empty (empty collections evaluate as falsy)

# 6
def format_word(word):
    if len(word) > 10:
        print(word.upper())
    else: 
        print(word)

format_word('tennis')           # tennis
format_word('programmers')      # PROGRAMMERS
format_word('jason hegarTy')    # JASON HEGARTY

# 7
def number_range(number):
    if number < 0:
        print(f'{number} is less than 0')
    elif number < 50:
        print(f'{number} is between 0 and 50')
    elif number <= 100:
        print(f'{number} is between 50 and 100')
    else:
        print(f'{number} is over 100')

number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0