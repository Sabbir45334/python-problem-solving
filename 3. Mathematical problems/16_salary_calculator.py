# Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20– 30%)(0-1lakh print k).

salary = float(input("Enter your basic salary: "))
HRA = salary * 0.10
DA = salary * 0.05
PF = salary * 0.03

if salary < 100000:
    tax = 0
elif 100000 <= salary <= 500000:
    tax = salary * 0.10
elif 500000 < salary <= 1000000:
    tax = salary * 0.20
else:
    tax = salary * 0.30

in_hand_salary = salary - HRA - DA - PF - tax
print("HRA:", HRA)
print("DA:", DA)
print("PF:", PF)
print("Tax:", tax)
print("In-hand salary:", in_hand_salary)