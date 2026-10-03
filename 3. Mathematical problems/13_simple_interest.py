# Write a program to find the simple interest when the value of principle,rate of interest and time period is given.
P = float(input("Enter the principle amount: "))
R = float(input("Enter the rate of interest (in percentage): "))
T = float(input("Enter the time period (in years): "))
# Calculate simple interest
SI = (P * R * T) / 100
print("The simple interest is:", SI)
