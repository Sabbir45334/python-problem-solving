# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("The transaction resulted in a profit of:", profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("The transaction resulted in a loss of:", loss)
else:
    print("The transaction resulted in neither profit nor loss.")