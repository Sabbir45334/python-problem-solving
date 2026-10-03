# User will provide 2 numbers you have to find the HCF of those 2 numbers

a = int(input("First number: "))
b = int(input("Second number: "))
hcf = 1
smaller = min(a, b)
for i in range(1, smaller + 1):
    if a % i == 0 and b % i == 0:
        hcf = i
print(hcf)


# different way to solve 

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# while num2 != 0:
#     remainder = num1 % num2
#     num1 = num2
#     num2 = remainder

# print("HCF is:", num1)