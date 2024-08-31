'''
8. Classes and Objects:
1.Avengers is a Marvel’s American Superheroes team, Now you want to
showcase your programming skills by representing the Avengers team using
classes. Create a class called Avenger and create these six superheroes using this
class.
2. super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk",
"Thor", "Hawkeye"]
3. Your Avenger class should have these properties:
1. Name
2. Age
3. Gender
4. Super Power
5. Weapon
4. Captain America has Super strength, Iron Man has Technology, Black Widow
is superhuman, Hulk has Unlimited Strength, Thor has super Energy and
Hawkeye has fighting skills as superpowers.
5. Weapons: Shield, Armor, Batons, No Weapon for hulk, Mjölnir, Bow, and
Arrows
6. Create methods to get the information about each superhero
7. Create a method is_leader() which will tell if the superhero is a leader or not.

'''

class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def get_info(self):
        return (f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Super Power: {self.super_power}\n"
                f"Weapon: {self.weapon}")

    def is_leader(self):
        leaders = ["Captain America"]
        return self.name in leaders

captain_america = Avenger("Captain America", 30, "Male", "Super Strength", "Shield")
iron_man = Avenger("Iron Man", 45, "Male", "Technology", "Armor")
black_widow = Avenger("Black Widow", 34, "Female", "Superhuman", "Batons")
hulk = Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon")
thor = Avenger("Thor", 1000, "Male", "Super Energy", "Mjölnir")
hawkeye = Avenger("Hawkeye", 35, "Male", "Fighting Skills", "Bow and Arrows")

avengers = [captain_america, iron_man, black_widow, hulk, thor, hawkeye]
for avenger in avengers:
    print(avenger.get_info())
    print(f"Is {avenger.name} a leader? {'Yes' if avenger.is_leader() else 'No'}\n")
