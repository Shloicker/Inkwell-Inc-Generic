class enemy(object):
    """The arguments here are as for item classes. HP is an integer. Note that enemies do not carry items but just have their own damage and armour values etc."""
    def __init__(self, name, description, hp, damage, armour, block):
        self.name = name
        self.description = description
        self.hp = hp
        self.damage = damage
        self.armour = armour
        self.block = block
    def is_alive(self):
        return self.hp >= 0
    def __str__(self):
        return self.name