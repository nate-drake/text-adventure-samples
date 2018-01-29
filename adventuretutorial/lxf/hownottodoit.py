print ("The Game that should not be")
print ("You are standing in a dimly lit room. To the west there is a door. In front of you there is a table. On the table is an apple.")
action = input("What do you do?")

if action == "move west":
    print("The door is locked.")
elif action == "move south":
    print("You cannot go that way.")
elif action == "move east":
    print("You cannot go that way.")
elif action == "move north":
    print("You cannot go that way.")
elif action == "take apple":
    print("You took the apple.")
        
        
    
