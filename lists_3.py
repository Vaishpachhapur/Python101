'''
3. List
1. You have a list of superheroes representing the Justice
League. justice_league = ["Superman","Batman","WonderWoman","Flash","Aquaman","Green Lantern"]
Perform the following tasks:
1. Calculate the number of members in the Justice League.
2. Batman recruited Batgirl and Nightwing as new members.
Add them to your list.
3. Wonder Woman is now the leader of the Justice League.
Move her to the beginning of the list.
4. Aquaman and Flash are having conflicts, and you need to
separate them. Choose either "Green Lantern" or "Superman"
and move them in between Aquaman and Flash.
5. The Justice League faced a crisis, and Superman decided to
assemble a new team. Replace the existing list with the following
new members: "Cyborg","Shazam","Hawkgirl","Martian Manhunter","Green Arrow".
6. Sort the Justice League alphabetically. The hero at the 0th
index will become the new leader.
(BONUS: Can you predict who the new leader will be?)
Your task is to write Python code to perform these operations on
the "justice_league" list. Display the list at each step to observe
the changes.

'''
#1
justice_league = ["Superman", "Batman", "Wonder Woman",
                  "Flash", "Aquaman", "Green Lantern"]

num_members = len(justice_league)
print("Number of members in the Justice League:", num_members)

#2
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("Justice League after adding Batgirl and Nightwing:", justice_league)

#3
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Justice League after Wonder Woman becomes the leader:", justice_league)

#4
justice_league.remove("Superman")
justice_league.insert(justice_league.index("Flash") + 1, "Superman")
print("Justice League after separating Aquaman and Flash:", justice_league)

#5
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("Justice League after replacing with new members:", justice_league)

#6
justice_league.sort()
print("Justice League after sorting alphabetically:", justice_league)

new_leader = justice_league[0]
print("The new leader of the Justice League is:", new_leader)















