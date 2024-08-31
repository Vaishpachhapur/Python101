'''1. Variables
1. Create a variable named pi and store the value 22/7 in it.
Now check the data type of this variable.
2. Create a variable called for and assign it a value 4. See what
happens and find out the reason behind the behavior that you
see.
3. Store the principal amount, rate of interest, and time in
different variables and then calculate the Simple Interest for 3
years. Formula: Simple Interest = P x R x T / 100
'''

#1
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))

#2
# for=4 # this will give you and error as it is a reserved keyword

#3
principal = 1000  # amount
rate_of_interest = 5  # in percentage
time = 3  # years
simple_interest = (principal * rate_of_interest * time) / 100
print("Simple Interest for 3 years:", simple_interest)

