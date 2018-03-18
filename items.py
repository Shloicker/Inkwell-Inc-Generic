class item(object):
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    def observe(self):
        return "{}\n-----\n{}\nValue: {}\n".format(self.name, self.description, self.value)
    def __str__(self):
        return "{}".format(self.name)

class weapon(item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        self.equipped_as_weapon = False
        super(weapon, self).__init__(name, description, value)
    def observe(self):
        return "{}\n-----\n{}\nValue: {}\nDamage: {}\n".format(self.name, self.description, self.value, self.damage)

class currency(item):
    pass                    #a dummy class so we can treat picking up currency differently to normal items (i.e it adds to our currency reserve rather than actually picking up an item)

class healing_consumable(item):
    def __init__(self, name, description, value, healing_amount):
        self.healing_amount = healing_amount
        super(healing_consumable, self).__init__(name, description, value)
    def observe(self):
        return "{}\n-----\n{}\nValue: {}\nHeals: {} health\n".format(self.name, self.description, self.value, self.health)

class armour(item):
    def __init__(self, name, description, value, armour_value):
        self.armour_value = armour_value
        self.equipped_as_armour = False
        super(armour, self).__init__(name, description, value)
    def equip_armour(self):
        for armour in player.inventory:
            armour.equipped_as_armour = False
        self.equipped_as_armour = True
    def observe(self):
        return "{}\n-----\n{}\nValue: {}\nArmour: {}\n".format(self.name, self.description, self.value, self.armour_value)

class shield(item):
    def __init__(self, name, description, value, block_value):
        self.block_value = block_value
        self.equipped_as_shield = False
        super(shield, self).__init__(name, description, value)
    def equip_shield(self):
        for shield in player.inventory:
            shield.equipped_as_shield = False
        self.equipped_as_shield = True
    def observe(self):
        return "{}\n-----\n{}\nValue: {}\nBlock: {}\n".format(self.name, self.description, self.value, self.block_value)