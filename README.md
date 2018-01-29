Code Samples
-------
These are code samples based on Phillip Johson's tutorial on create your own Python Text Adventure (https://github.com/phillipjohnson/text-adventure-tut.git). 

At the time of writing, the modifications to the original game include:
- Changed 'LootRoom' code in tiles.py to stop multiple items being added to the inventory.
- Added weapon 'Axe' in items.py 
- Added a 'FindAxeRoom' in tiles.py to allow players to pick up the axe.
- Modified items.py to create a new 'Armour' superclass and also created a 'Shield' object in this class.
- Modified enemy combat system in 'tiles.py' to reduce damage caused if player is causing armour. Currently the game selects the player's "best" armour just as it selects their "best" weapon for combat. 

Tutorial
--------
For an in-depth tutorial, please see [How to Write a Text Adventure in Python](http://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python/) or purchase 'Make your Own Python Text Adventure' (https://www.amazon.com/Make-Your-Python-Text-Adventure/dp/1484232305?)
