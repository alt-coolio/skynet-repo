
# Online Python - IDE, Editor, Compiler, Interpreter

# Creation of a list with a defined range
import os
created_list = range(0, 1000)

# Initialized even_number and odd_number lists
even_number = []
odd_number = []

# Sorts even and odd number accordingly
for number in created_list:
    # print(i%2)
    if (number % 2 > 0):
        odd_number.append(number)
    else:
        even_number.append(number)

# Sorted results are printed to the screen
print(even_number, '\n\n\n', odd_number)
print('\n')
print(even_number[slice(0, 5)])
print('\n')
print(len(even_number), len(odd_number))
