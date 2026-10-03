# #Write a program that can multiply 2 numbers provided by the user without using the * operator

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = 0
for i in range(1,num2+1):
    sum += num1
    print(f"After adding {num1} for {i} times, the sum is: {sum}")

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# for i in range(1, num2+1):
#     total = sum([num1 for _ in range(i)])
# print(f"The product of {num1} and {num2} is: {total}")


# by creating a list of num1 repeated num2 times and then summing the list to get the product.
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# d = [num1 for _ in range(num2)]
# print(d)
# print(f"The product of {num1} and {num2} is: {sum(d)}")