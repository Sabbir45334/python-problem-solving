# This program swaps two numbers without using a temporary variable.
# my one
# a = float(input("Enter a number: "))
# b = float(input("Enter another number: "))  
# a, b = b, a

# print("After swapping:")
# print("a =", a)
# print("b =", b)


# edited one
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

first_number, second_number = second_number, first_number

print("After swapping:")
print("First number:", first_number)
print("Second number:", second_number)