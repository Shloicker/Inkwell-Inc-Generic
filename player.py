import items, enemies, random, currency_config, map_tiles

class player():
    def __init__(self, inventory, currency_amount):
        self.inventory = inventory
        self.currency_amount = currency_amount
        self.hp = 100
#         self.location_x, self.location_y = world.starting_location
        self.victory = False

    def is_not_dead(self):
        return self.hp > 0

    def take_inventory(self):
        return '\n'.join('{}'.format(item) for item in self.inventory) + "\nYou have {} {}.".format(self.currency_amount, currency_config.currency)

    def observe(self, subject):
        if issubclass(type(subject), items.item):
            return subject.observe_item()
        if issubclass(type(subject), enemies.enemy):
            return subject.observe_enemy()
        if issubclass(type(subject), map_tiles.map_tile):
            return subject.show_room_text()
        return "There is no such thing."

    def equip_weapon(self, weapon_to_be_equipped):
        if issubclass(type(weapon_to_be_equipped), items.weapon):
            for item in self.inventory:
                if issubclass(type(item), items.weapon):
                    item.equipped_as_weapon = False
            weapon_to_be_equipped.equipped_as_weapon = True
            return "You have equipped {} as weapon.".format(weapon_to_be_equipped)
        return "That is not a weapon."

    def equip_armour(self, armour_to_be_equipped):
        if issubclass(type(armour_to_be_equipped), items.armour):
            for item in self.inventory:
                if issubclass(type(item), items.armour):
                    item.equipped_as_armour = False
            armour_to_be_equipped.equipped_as_armour = True
            return "You have equipped {} as armour.".format(armour_to_be_equipped)
        return "That is not armour."

    def equip_shield(self, shield_to_be_equipped):
        if issubclass(type(shield_to_be_equipped), items.shield):
            for item in self.inventory:
                if issubclass(type(item), items.shield):
                    item.equipped_as_shield = False
            shield_to_be_equipped.equipped_as_shield = True
            return "You have equipepd {} as shield.".format(shield_to_be_equipped)
        return "That is not a shield."

    def view_equipped_items(self):
        equipped_items = []
        for item in self.inventory:
            if issubclass(type(item), items.weapon):
                if item.equipped_as_weapon:
                    equipped_items.append("{} equipped as weapon.".format(item))
            if issubclass(type(item), items.armour):
                if item.equipped_as_armour:
                    equipped_items.append("{} equipped as armour.".format(item))
            if issubclass(type(item), items.shield):
                if item.equipped_as_shield:
                    equipped_items.append("{} equipped as shield.".format(item))
        return '\n'.join('{}'.format(string) for string in equipped_items)

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
            if issubclass(type(item), items.weapon):
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