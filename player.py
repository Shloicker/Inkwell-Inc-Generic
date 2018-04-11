import items, enemies, random, currency_config, world

class player():
    def __init__(self, inventory, currency_amount):
        self.inventory = inventory
        self.currency_amount = currency_amount
        self.hp = 100
        self.location_x = 0
        self.location_y = 0
        self.victory = False

    def is_not_dead(self):
        return self.hp > 0

    def take_inventory(self):
        return '\n'.join('{}'.format(item) for item in self.inventory) + "\n{} {}.".format(self.currency_amount, currency_config.currency)

    def observe(self, subject):
        if issubclass(type(subject), items.item):
            return subject.observe_item()
        if issubclass(type(subject), enemies.enemy):
            return subject.observe_enemy()
#         if issubclass(type(subject), map_tiles.map_tile):
#             if issubclass(type(subject), map_tiles.loot_room):
#                 return subject.view_tile_inventory()
#             if issubclass(type(subject), map_tiles.shop_room):
#                 return subject.show_shop_inventory()
        return "There is no such thing."

    def look_around(self):
        return world.tile_exists(self.location_x, self.location_y).view_tile_inventory()

    def equip(self, item_to_be_equipped):
        if issubclass(type(item_to_be_equipped), items.weapon):
            for item in self.inventory:
                if issubclass(type(item), items.weapon):
                    item.equipped_as_weapon = False
            item_to_be_equipped.equipped_as_weapon = True
            return "You have equipped {} as weapon.".format(item_to_be_equipped)
        if issubclass(type(item_to_be_equipped), items.armour):
            for item in self.inventory:
                if issubclass(type(item), items.armour):
                    item.equipped_as_armour = False
            item_to_be_equipped.equipped_as_armour = True
            return "You have equipped {} as armour.".format(item_to_be_equipped)
        if issubclass(type(item_to_be_equipped), items.shield):
            for item in self.inventory:
                if issubclass(type(item), items.shield):
                    item.equipped_as_shield = False
            item_to_be_equipped.equipped_as_shield = True
            return "You have equipped {} as shield.".format(item_to_be_equipped)

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
        return world.tile_exists(self.location_x, self.location_y).show_room_text()

    def move_north(self):
        return self.move(dx=0, dy=-1)

    def move_south(self):
        return self.move(dx=0, dy=1)

    def move_east(self):
        return self.move(dx=1, dy=0)

    def move_west(self):
        return self.move(dx=-1, dy=0)

    def pick_up(self, item):
        world.tile_exists(self.location_y, self.location_y).pick_up_item(self, item)

    def drop(self, item):
        return world.tile_exists(self.location_y, self.location_y).drop_item(self, item)

    def buy(self, item):
        return world.tile_exists(self.location_y, self.location_y).buy_item(self, item)

    def sell(self, item):
        return world.tile_exists(self.location_y, self.location_y).sell_item(self, item)

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
                return "You hit {} with {}, dealing {} damage!\n {} now has {} HP.".format(enemy, equipped_weapon, dealt_damage, enemy, enemy.hp) + "\n" + world.tile_exists(self.location_x, self.location_y).enemy_attack(self)
        return "Your attack misses!\n {} still has {} HP.".format(enemy, enemy.hp) + "\n" + world.tile_exists(self.location_x, self.location_y).enemy_attack(self)

    def flee(self):
        world.tile_exists(self.location_x, self.locaton_y).adjacent_moves()
        r = random.randint(0, len(moves) - 1)
        return self.do_action(moves[r])

    def do_action(self, action, *args):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            return action_method(*args)