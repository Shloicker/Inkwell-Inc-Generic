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

    def observe_item(self, item):
        return item.observe()

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
                if item.equipped_as_weapon:
                    equipped_items.append("{} equipped as weapon.".format(item))
            if type(item) is items.armour:
                if item.equipped_as_armour:
                    equipped_items.append("{} equipped as armour.".format(item))
            if type(item) is items.shield:
                if item.equipped_as_shield:
                    equipped_items.append("{} equipped as shield.".format(item))
        return '\n'.join('{}'.format(item) for item in equipped_items)

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        return world.tile_exists(self.location_x, self.location_y).intro_text()

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        for item in self.inventory:
            if type(item) is items.weapon:
                if item.equipped_as_weapon:
                    equipped_weapon = item
        if random.randint(0, 100) >= enemy.block:
            enemy_resistance = (100 - enemy.armour)
            dealt_damage = int(round((enemy_resistance * equipped_weapon.damage) / 100))
            enemy.hp -= dealt_damage
            if not enemy.is_alive():
                return "You hit {} with {}, dealing {} damage - a killing blow!".format(enemy, equipped_weapon, dealt_damage)
            else:
                return "You hit {} with {}, dealing {} damage!\n {} now has {} HP.".format(enemy, equipped_weapon, dealt_damage, enemy, enemy.hp)
        return "Your attack misses!\n {} still has {} HP.".format(enemy, enemy.hp)

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            return action_method(**kwargs)