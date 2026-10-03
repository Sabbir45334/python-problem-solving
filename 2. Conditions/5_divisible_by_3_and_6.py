# Write  a program that will tell whether the given number is divisible by 3 & 6.

x = int(input("enter the num:"))   
while True:
    if x % 3 == 0 and x % 6 == 0:
        print("The number is divisible by 3 and 6.",)
        break
    else:
        print("The number is not divisible by 3 and 6.",)
        print("Try again.")
        x = int(input("enter the num:"))