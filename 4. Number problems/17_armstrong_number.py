# Write a program that will check whether the number is armstrong number or not.
num = int(input("Enter a number: "))
num_str = str(num)
num_digits = len(num_str)
print("The number of digits in the number is:", num_digits)
sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
print("The sum of the digits raised to the power of", num_digits, "is:", sum_of_powers)
if sum_of_powers == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")