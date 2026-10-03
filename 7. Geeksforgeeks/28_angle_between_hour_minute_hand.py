# Find the angle between the hour and minute hands of a clock.

def find_angle(hour, minute):
    # Convert hour to 12-hour format
    hour = hour % 12

    # Calculate the position of each hand
    hour_angle = (hour * 30) + (minute * 0.5)
    minute_angle = minute * 6

    # Find the difference
    angle = abs(hour_angle - minute_angle)

    # Return the smaller angle
    return min(angle, 360 - angle)


hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))

print("Angle:", find_angle(hour, minute))