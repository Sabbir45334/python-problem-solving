# Write a program to print all the unique combinations of 1,2,3 and 4

from itertools import permutations

numbers = [1, 2, 3, 4]

for combination in permutations(numbers):
    print(combination)