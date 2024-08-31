'''
6. Dictionary
1. Create a list of your friends' names. The list should have at least 5 
names.
Create a list of tuples. Each tuple should contain a friend's name and the
length of the name.
For example, if someone’s name is Aditya, the tuple would be: ('Aditya', 6)
2.You and your partner are planning a trip, and you want to track expenses.
Create two dictionaries, one for your expenses and one for your partner's
expenses. Each dictionary should contain at least 5 expense categories
and their corresponding amounts.
For example:
Your expenses
your_expenses = {
"Hotel": 1200,
"Food": 800,
"Transportation": 500,
"Attractions": 300,
"Miscellaneous": 200
}
Your partner's expenses
partner_expenses = {
"Hotel": 1000,
"Food": 900,
"Transportation": 600,
"Attractions": 400,
"Miscellaneous": 150
}
Calculate the total expenses for each of you and print the results.
Determine who spent more money overall and print the result.
Find out the expense category where there is a significant difference 
in spending between you and your partner.
Print the category and the difference.

'''

#1
friends = ["Akash", "Sindhu", "Siddharth", "Shreyas", "Yashaswini"]
friends_name_length = [(friend, len(friend)) for friend in friends]
print("Friends and their name lengths:", friends_name_length)

#2
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}
partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}
your_total_expenses = sum(your_expenses.values())
partner_total_expenses = sum(partner_expenses.values())
print(f"Your total expenses: {your_total_expenses}")
print(f"Your partner's total expenses: {partner_total_expenses}")
if your_total_expenses > partner_total_expenses:
    print("You spent more money overall.")
elif your_total_expenses < partner_total_expenses:
    print("Your partner spent more money overall.")
else:
    print("Both spent the same amount of money.")
significant_difference = {}
for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > 100: 
        significant_difference[category] = difference
if significant_difference:
    for category, difference in significant_difference.items():
        print(f"Significant difference in {category}: {difference}")
else:
    print("No significant differences in spending were found.")

