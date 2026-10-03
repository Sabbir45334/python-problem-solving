# Write a program that will take three digits num from the user and add the square of each digit.

x = int(input("enter 3 digit num:"))
while x < 100 or x > 999:
    print("Please enter a three-digit number.")
    x = int(input("enter 3 digit num:"))
d = [int(x) for x in str(x)]
sum_of_squares = sum(digit ** 2 for digit in d)
print("The sum of the squares of the digits is:", sum_of_squares)

