class Weapon:        
    def __repr__(self):
        return self.name
    
class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A rusty looking dagger."
        self.damage = 5
        
class Axe(Weapon):
    def __init__(self):
        self.name = "Axe"
        self.description = "A wickedly sharp-looking axe made of black metal."
        self.damage = 15

myinventory = [Dagger(),'Gold(10)','apple']
print ("The Game that should not be")
print ("You are standing in a dimly lit room. To the west there is a door. In front of you there is a table. On the table is an axe.")

def move_player():
    return input("What do you do?")

action = move_player()

if action == "move west":
    print("The door is locked.")
elif action == "move south":
    print("You cannot go that way.")
elif action == "move east":
    print("You cannot go that way.")
elif action == "move north":
    print("You cannot go that way.")
elif action == "take axe":
    print("You took the axe.")
    myinventory.append(Axe())
elif action == "i":
    print(myinventory)   
else:
    print("You can't do that.")


        
        
    
