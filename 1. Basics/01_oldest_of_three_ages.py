# User will input (3ages).Find the oldest one

# Find the oldest among three ages

age1 = int(input("Enter first age: "))
age2 = int(input("Enter second age: "))
age3 = int(input("Enter third age: "))

oldest = max(age1, age2, age3)

print("The oldest age is:", oldest)