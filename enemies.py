class enemy(object):
    def __init__(self, name, description, hp, damage, armour, block):
        self.name = name
        self.description = description
        self.hp = hp
        self.damage = damage
        self.armour = armour
        self.block = block
    def is_alive(self):
        return self.hp >= 0