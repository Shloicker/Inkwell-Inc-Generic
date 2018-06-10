import text_adventure.world as world

class enemy(object):
    """The arguments here are as for item classes. HP is an integer. Note that enemies do not carry items but just have their own damage and armour values etc."""
    def __init__(self, name, description, hp, damage, armour, block):
        self.name = name
        self.description = description
        self.hp = hp
        self.damage = damage
        self.armour = armour
        self.block = block
        world._objects[name.lower()] = self
        world.objects_list.append(self)

    def is_alive(self):
        return self.hp >= 0

    def observe_enemy(self):
        return "{}\n-----\n{}\nHealth: {}\nDamage: {}\nArmour: {}\nBlock: {}".format(self.name, self.description, self.hp, self.damage, self.armour, self.block)

    def __str__(self):
        return self.name
