# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
while True:
    num = int(input("Enter a four-digit number: "))
    if len(str(num)) != 4:
        print("Invalid input. Please enter a four-digit number.")
        num = int(input("Enter a four-digit number: "))
    else:
        print("The number you entered is:", num)
   
    reversed_num = int(str(num)[::-1])
    print("The reversed number is:", reversed_num)

    if num == reversed_num:
        print("The reverse is false.")
    else:
        print("The reverse is true.")
        break
