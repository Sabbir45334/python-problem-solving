# # Write a program to find the sum of first n numbers, where n will be provided by the user. Eg if the user provides n=10 the output should be 55.

num = int(input("Enter a number: "))
if num < 1:
    print("Please enter a positive integer.")
else:
    total = sum(range(1, num + 1))
    print(f"The sum of the first {num} numbers is: {total}")



# they will provide the range of numbers and the program will find the sum of all the numbers in that range. Eg if the user provides 1 to 10 the output should be 55.

# start = int(input("Enter the starting number: "))
# end = int(input("Enter the ending number: "))
# if start > end:
#     print("Please enter a valid range.")
# else:
#     total = sum(range(start, end + 1))
#     print(f"The sum of numbers from {start} to {end} is: {total}")

