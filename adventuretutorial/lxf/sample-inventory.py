myinventory = ['Dagger','Gold(10)','apple']
print ("The Game that should not be")
print ("You are standing in a dimly lit room. To the west there is a door. In front of you there is a table. On the table is a rusty key.")

def move_player():
    return input("What do you do?")

action = move_player()

if action == "move west":
    print("The door is locked.")
    if myinventory.count("key") == 0:
        print("You do not have a key.")
    else:
        print("You unlock the door with the key.")
elif action == "move south":
    print("You cannot go that way.")
elif action == "move east":
    print("You cannot go that way.")
elif action == "move north":
    print("You cannot go that way.")
elif action == "take key":
    print("You took the rusty key.")
    myinventory.append("key")
elif action == "i":
    print(myinventory)   
else:
    print("You can't do that.")


        
        
    
