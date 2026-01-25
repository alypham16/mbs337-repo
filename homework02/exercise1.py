# Exercise Prompt: Create a list of ~10 different integers. 
# Write a function (using modulus and conditionals) to determine if each integer is even or odd. 
# Print to screen each digit followed by the word ‘even’ or ‘odd’ as appropriate.

from random import randint
int_lst = [randint(1, 100) for _ in range(10)]

def even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

for number in int_lst:
    even_or_odd(number)
