'''
4. If Condition
1. Write a program to determine the BMI Category based on user input.
Ask the user to:
Enter height in meters
Enter weight in kilograms
Calculate BMI using the formula: BMI = weight / (height)2
Use the following categories:
If BMI is 30 or greater, print "Obesity"
If BMI is between 25 and 29, print "Overweight"
If BMI is between 18.5 and 25, print "Normal"
If BMI is less than 18.5, print "Underweight"
Example:
Enter height in meters: 1.75
Enter weight in kilograms: 70
Output: "Normal"
2. Write a program to determine which country a city belongs to. Given
list of cities per country:
Australia = ["Sydney"
,
"Melbourne"
,
"Brisbane"
,
"Perth"]
UAE = ["Dubai"
,
"Abu Dhabi"
,
"Sharjah"
,
"Ajman"]
India = ["Mumbai"
,
"Bangalore"
,
"Chennai"
,
"Delhi"]
Ask the user to enter a city name and print the corresponding country.
Example:
Enter a city name: "Abu Dhabi"
Output: "Abu Dhabi is in UAE"
3. Write a program to check if two cities belong to the same country.
Ask the user to enter two cities and print whether they belong to the
same country or not.
Example:
Enter the first city: "Mumbai"
Enter the second city: "Chennai"
Output: "Both cities are in India"
Example:
Enter the first city: "Sydney"
Enter the second city: "Dubai"
Output: "They don't belong to the same country"
'''

#1
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)
if bmi >= 30:
    category = "Obesity"
elif 25 <= bmi < 30:
    category = "Overweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
else:
    category = "Underweight"

print(f"BMI: {bmi:.2f}")
print("Output:", category)

#2
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ")

if city in australia:
    country = "Australia"
elif city in uae:
    country = "UAE"
elif city in india:
    country = "India"
else:
    country = "Unknown"

if country != "Unknown":
    print(f"{city} is in {country}")
else:
    print(f"{city} is not in the list of known cities.")

#3
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

if (city1 in australia and city2 in australia) or \
   (city1 in uae and city2 in uae) or \
   (city1 in india and city2 in india):
    print(f"Both {city1} and {city2} are in the same country.")
else:
    print(f"{city1} and {city2} don't belong to the same country.")
