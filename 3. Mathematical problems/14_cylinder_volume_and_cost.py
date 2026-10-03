# Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.

import math

r = float(input("Enter the radius of the cylinder(cm): "))
h = float(input("Enter the height of the cylinder(cm): "))

# Calculate the volume of the cylinder
volume = math.pi * r**2 * h

# Calculate the cost
cost = volume/1000 * 40   # Convert volume from cubic centimeters to liters

print("The volume of the cylinder is:", volume, "Cm³")
print("The cost is:", cost)