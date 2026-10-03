# Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.

angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("The angles can form a triangle.")
else:
    print("The angles cannot form a triangle.")