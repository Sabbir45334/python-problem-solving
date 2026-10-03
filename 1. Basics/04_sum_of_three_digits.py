# Q-4. Write a Python program to calculate the sum of the digits of a three-digit number.


# solved by pthonic thinking 
# num = int(input("Enter a three digit number: "))

# List = [int(digit) for digit in str(num)]
# print("The digits of the number are:", List)

# c= List[0] + List[1] + List[2]
# print("The sum of the digits is:", c)


# solved by Loop
# num = int(input("Enter a three digit number: "))
# c = 0
# while num > 0:
#     c += num % 10
#     num //= 10
# print("The sum of the digits is:", c)


## solved by mathmatical thinking
while True:
    num = int(input("Enter a three-digit number: "))

    if 100 <= num <= 999:
        a = num // 100
        b = (num // 10) % 10
        c = num % 10
        total = a + b + c

        print("The sum of the digits is:", total)
        break
    else:
        print("Please enter a three-digit number.")
        print("Try again.")