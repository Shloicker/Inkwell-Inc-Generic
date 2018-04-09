class item(object):
    """A generic item with no utility other than selling at shops. To create a generic item (an instance of this class) you would write 'item = text_adventure.item(name, description, value).' The name and description both have to be strings (i.e. words in quotations "") while the value has to be an integer and the arguments must be in the order as presented in the __init__ function of each class (directly below)."""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def observe_item(self):
        return "{}\n-----\n{}\nValue: {}\n".format(self.name, self.description, self.value)

    def __str__(self):
        return "{}".format(self.name)

class weapon(item):
    """Similar to generic item - you simply write 'text_adventure.weapon(...)' for this one. It takes a fourth argument, damage, which must be an integer."""
    def __init__(self, name, description, value, damage):
        self.damage = damage
        self.equipped_as_weapon = False
        super(weapon, self).__init__(name, description, value)

    def observe_item(self):
        return "{}\n-----\n{}\nValue: {}\nDamage: {}\n".format(self.name, self.description, self.value, self.damage)

class healing_consumable(item):
    """Self explanatory - healing amount is an integer between 0 and 100 (player has 100 health for reference)."""

    def __init__(self, name, description, value, healing_amount):
        self.healing_amount = healing_amount
        super(healing_consumable, self).__init__(name, description, value)

    def observe_item(self):
        return "{}\n-----\n{}\nValue: {}\nHeals: {} health\n".format(self.name, self.description, self.value, self.health)

class armour(item):
    """Armour value is integer between 0 and 100. It reduces incoming damage by that percentage (i.e. 20 armour means damage is reduced by 20%)."""
    def __init__(self, name, description, value, armour_value):
        self.armour_value = armour_value
        self.equipped_as_armour = False
        super(armour, self).__init__(name, description, value)

    def observe_item(self):
        return "{}\n-----\n{}\nValue: {}\nArmour: {}\n".format(self.name, self.description, self.value, self.armour_value)

class shield(item):
    """Again block value is between 0 and 100. It is the percentage chance to dodge/block an attack."""
    def __init__(self, name, description, value, block_value):
        self.block_value = block_value
        self.equipped_as_shield = False
        super(shield, self).__init__(name, description, value)

    def observe_item(self):
        return "{}\n-----\n{}\nValue: {}\nBlock: {}\n".format(self.name, self.description, self.value, self.block_value)