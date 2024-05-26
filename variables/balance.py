"""This program will output the balance in 5 years 
based on 5% compound interest growth each year.
"""
balance = 1000
interest_rate = 1.05
for year in range(1,6): 
    balance *= interest_rate
    print(f'Year {year} balance: £{balance:.2f}')
print(f'Your final balance is: ${balance:.2f}.')