import random
import items
import enemies

class player():
    def __init__(self, inventory):
        self.inventory = inventory
        self.hp = 100
#         self.location_x, self.location_y = world.starting_location
        self.victory = False

    def is_not_dead(self):
        return self.hp > 0

    def take_inventory(self):
        return '\n'.join('{}'.format(item) for item in self.inventory)

    def equip_weapon(self, weapon_to_be_equipped):
        for item in self.inventory:
            if type(item) is items.weapon:
                item.equipped_as_weapon = False
        weapon_to_be_equipped.equipped_as_weapon = True

    def equip_armour(self, armour_to_be_equipped):
        for item in self.inventory:
            if type(item) is items.armour:
                item.equipped_as_armour = False
        armour_to_be_equipped.equipped_as_armour = True

    def equip_shield(self, shield_to_be_equipped):
        for item in self.inventory:
            if type(item) is items.shield:
                item.equipped_as_shield = False
        shield_to_be_equipped.equipped_as_shield = True

    def view_equipped_items(self):
        equipped_items = []
        for item in self.inventory:
            if type(item) is items.weapon:
                if item.equipped_as_weapon == True:
                    equipped_items.append("{} equipped as weapon.".format(item))
            if type(item) is items.armour:
                if item.equipped_as_armour == True:
                    equipped_items.append("{} equipped as armour.".format(item))
            if type(item) is items.shield:
                if item.equipped_as_shield == True:
                    equipped_items.append("{} equipped as shield.".format(item))
        return '\n'.join('{}'.format(item) for item in equipped_items)

#     def move(self, dx, dy):
#         self.location_x += dx
#         self.location_y += dy
#         return world.tile_exists(self.location_x, self.location_y).intro_text()

#     def move_north(self):
#         self.move(dx=0, dy=-1)

#     def move_south(self):
#         self.move(dx=0, dy=1)

#     def move_east(self):
#         self.move(dx=1, dy=0)

#     def move_west(self):
#         self.move(dx=-1, dy=0)

    def attack(self, enemy):
        for item in self.inventory:
            if type(item) is items.weapon:
                if item.equipped_as_weapon == True:
                    equipped_weapon = item
        if random.randint(0, 100) >= enemy.block:
            enemy_resistance = (100 - enemy.armour)
            dealt_damage = int(round((enemy_resistance * equipped_weapon.damage) / 100))
            enemy.hp -= dealt_damage
#             return enemy_resistance, dealt_damage, enemy.hp, enemy.armour
            if not enemy.is_alive():
                return "You hit {} with {}, dealing {} damage - a killing blow!".format(enemy.name, equipped_weapon.name, dealt_damage)
            else:
                return "You hit {} with {}, dealing {} damage!\n {} now has {} HP.".format(enemy.name, equipped_weapon.name, dealt_damage, enemy.name, enemy.hp)
        return "Your attack misses!\n {} still has {} HP.".format(enemy.name, enemy.hp)
