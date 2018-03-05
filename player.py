import items

class player():
    def __init__(self):
        self.inventory = []
        self.hp = 100
        self.location = world.starting_location
        self.victory = false
    def is_not_dead(self):
        return self.hp > 0
    def take_inventory(self):
        for item in self.inventory:
            print(item, '\n')