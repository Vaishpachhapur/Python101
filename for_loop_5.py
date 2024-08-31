'''
5. For Loop:
1. Using a for loop, simulate rolling a sixsided die multiple times (at least 20
times).
Count and print the following statistics:
How many times you rolled a 6
How many times you rolled a 1
How many times you rolled two 6s in a row
2. Imagine you are doing a workout routine, and you have to complete 100
jumping jacks.
Write a program that:
Asks you to perform 10 jumping jacks at a time.
After each set, it asks, "Are you tired?"
If you reply "yes" or "y," it should ask if you want to skip the remaining sets.
If you reply "yes" or "y," it should break and print, "You completed a total of
jumping jacks."
For example, if you did only 30 jumping jacks and answered "yes," the program
will break and print, "You completed a total of 30 jumping jacks."
If you reply "no" or "n," it should continue and display how many jumping jacks
are remaining. After that, ask you again, "Are you tired?"
For example, if you answered "no," it should display that 70 jumping jacks are
remaining and ask you again, "Are you tired?"
If you reply "no" or "n," it should continue and display how many jumping jacks
are remaining. After that, ask you again, "Are you tired?"
For example, if you answered "no," it should display that 70 jumping jacks are
remaining and ask you again, "Are you tired?"
If you complete all 100 jumping jacks, it should print, "Congratulations! You
completed the workout," and stop the program

'''

#1
import random
count_6 = 0
count_1 = 0
count_two_6s_in_a_row = 0
previous_roll = None

for _ in range(20):
    roll = random.randint(1, 6)  # roll the die

    if roll == 6:
        count_6 += 1
    
    if roll == 1:
        count_1 += 1
    
    if previous_roll == 6 and roll == 6:
        count_two_6s_in_a_row += 1

    previous_roll = roll

    print(f"Roll: {roll}")  

print(f"\nTotal times 6 was rolled: {count_6}")
print(f"Total times 1 was rolled: {count_1}")
print(f"Total times two 6s were rolled in a row: {count_two_6s_in_a_row}")

#2
total_jumping_jacks = 100
jumping_jacks_per_set = 10
completed_jumping_jacks = 0

while completed_jumping_jacks < total_jumping_jacks:
    completed_jumping_jacks += jumping_jacks_per_set
    print(f"You completed {completed_jumping_jacks} jumping jacks.")
    response = input("Are you tired? (yes/y or no/n): ").lower()
    if response in ["yes", "y"]:
        skip_response = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()

        if skip_response in ["yes", "y"]:
            print(f"You completed a total of {completed_jumping_jacks} jumping jacks.")
            break
        else:
            print(f"{total_jumping_jacks - completed_jumping_jacks} jumping jacks remaining.")
    else:
        if completed_jumping_jacks < total_jumping_jacks:
            print(f"{total_jumping_jacks - completed_jumping_jacks} jumping jacks remaining.")

if completed_jumping_jacks >= total_jumping_jacks:
    print("Congratulations! You completed the workout.")
