# Write a program that will determine weather when the value of temperature and humidity is provided by the user.

temperature = float(input("Enter the temperature in Celsius: "))
humidity = float(input("Enter the humidity percentage: "))
if temperature >= 30 and humidity >=90:
    print("The weather is hot and humid.")
elif temperature >= 30 and humidity < 90:
    print("The weather is hot and dry.")   
elif temperature < 30 and humidity >= 90:
    print("The weather is cool and humid.")
elif temperature < 30 and humidity < 90:
    print("The weather is cool and dry.")
else:
    print("The weather is neither hot nor cool.")
