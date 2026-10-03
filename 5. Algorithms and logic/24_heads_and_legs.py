# Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
total_heads = int(input("Enter the total number of heads: "))
total_legs = int(input("Enter the total number of legs: "))

# Assuming each dog has 4 legs and each chicken has 2 legs
# Let d be the number of dogs and c be the number of chickens
# d + c = total_heads
# so d= (total_heads - c)
# 4d + 2c = total_legs (in terms of c)
# 4d + 2(total_heads - d) = total_legs
# 2d = total_legs - 2(total_heads)
# so d = (total_legs - 2 * total_heads) // 2
# so c = total_heads - d

#  Solving the system of equations
while True:
    if total_legs % 2 != 0 or total_heads > total_legs // 2 or total_legs > total_heads * 4:
        print("Invalid input. Please enter valid numbers of heads and legs.")
        total_heads = int(input("Enter the total number of heads: "))
        total_legs = int(input("Enter the total number of legs: "))
    else:
        break

d = (total_legs - 2 * total_heads) // 2
c = total_heads - d

print(f"Number of dogs: {d}")
print(f"Number of chickens: {c}")