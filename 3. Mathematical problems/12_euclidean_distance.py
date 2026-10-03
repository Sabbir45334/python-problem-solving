# Write a program to find the euclidean distance between two coordinates.

# with using math module
import math
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))
x_diff = x2 - x1
y_diff = y2 - y1
distance = math.sqrt(x_diff ** 2 + y_diff ** 2)

print("The Euclidean distance between the two points is:", distance)
