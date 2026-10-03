# Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.

num = int(input("Enter a 4-digit number: "))
while num < 1000 or num > 9999:
    choice = input("would you like to try again? (y/n): ")
    if choice == "n":
        exit()
    elif choice == "y":
        print("Please enter a 4-digit number.")
    else:
        print("Invalid choice.")
        exit()
    num = int(input("Enter a 4-digit number: "))
num_str = str(num)
num_digits = len(num_str)
sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
if sum_of_powers == num:
    print(num, "is a narcissistic number.")
else:
    print(num, "is not a narcissistic number.")