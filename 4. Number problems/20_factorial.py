# Write a program that can find the factorial of a given number provided by the user.

n = int(input("Enter a number to find its factorial: "))

while n < 0:
    print("Factorial is not defined for negative numbers, please enter a non-negative integer.")
    n = int(input("Enter a number to find its factorial: "))
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is: {factorial}")
            