'''
2. Numbers
1. Write a function that takes two arguments, 145 and 'o', and uses the 
`format` function to return a formatted string. Print the
result. Try to identify the representation used.
2. In a village, there is a circular pond with a radius of 84 meters.
Calculate the area of the pond using the formula: Circle Area = π
r^2. (Use the value 3.14 for π) Bonus Question: If there is exactly
1.4 liters of water in a square meter, what is the total amount of
water in the pond? Print the answer without any decimal point in
it. Hint: Circle Area = π r^2 Water in the pond = Pond Area
Water per Square Meter
3. If you cross a 490meterlong street in 7 minutes, calculate your
speed in meters per second. Print the answer without any decimal
point in it. Hint: Speed = Distance / Time
'''
#1
def format_number(number, base):
    if base == 'o':
        # Format the number as an octal
        formatted_number = format(number, 'o')
    else:
        formatted_number = str(number)
    return formatted_number

result = format_number(145, 'o')
print("Formatted number:", result)

#2
radius = 84  
pi = 3.14 

pond_area = pi * (radius ** 2)
water_per_square_meter = 1.4 # liters
total_water = pond_area * water_per_square_meter

print("Area of the pond:", pond_area)
print("Total amount of water in the pond:", int(total_water))

#3
distance = 490  # meters
time_in_minutes = 7  # in minutes
# converting time to seconds
time_in_seconds = time_in_minutes * 60  # 7 minutes = 420 seconds
speed = distance / time_in_seconds

print("Speed in meters per second:", int(speed))


