"""Describes the items in the game."""
__author__ = 'Phillip Johnson'


class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
    
class Armour(Item):
    def __init__(self, name, description, value, protection):
        self.protection = protection
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nProtection: {}".format(self.name, self.description, self.value, self.protection)

class Shield(Armour):
    def __init__(self):
        super().__init__(name="Shield",
                         description="A leather shield which reduces any HP damage in combat by 3 points.",
                         value=8,
                         protection=3)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)

class Axe(Weapon):
    def __init__(self):
        super().__init__(name="Axe",
                         description="A wickedly sharp looking axe made of black metal.",
                         value=15,
                         damage=15)

class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)
