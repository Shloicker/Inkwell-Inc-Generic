import items, enemies, player, random

class map_tile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class starting_room(map_tile):
    def __init__(self, x, y, room_text):
        self.room_text = room_text
        super(starting_room, self).__init__(x, y)

    def show_room_text(self):
        return self.room_text

class loot_room(map_tile):
    def __init__(self, x, y, room_text, tile_inventory):
        self.room_text = room_text
        self.tile_inventory = tile_inventory
        super(loot_room, self).__init__(x, y)

    def show_room_text(self):
        return self.room_text

    def view_tile_inventory(self):
        return '\n'.join('{}'.format(item) for item in self.tile_inventory)

    def pick_up_item(self, player, item):
        if issubclass(type(item), items.item):
            if item in self.tile_inventory:
                player.inventory.append(item)
                self.tile_inventory.remove(item)
                return "You pick up {}.".format(item.name)
            return "There is no {} here.".format(item.name)
        return "That is not an item."

    def drop_item(self, player, item):
        if issubclass(type(item), items.item):
            if item in player.inventory:
                self.tile_inventory.append(item)
                player.inventory.remove(item)
                return "You drop {}".format(item.name)
            return "There is no {} in your inventory.".format(item.name)
        return "That is not an item."

class shop_room(map_tile):
    def __init__(self, x, y, room_text, shop_inventory, shop_currency_amount):
        self.room_text = room_text
        self.shop_inventory = shop_inventory
        self.shop_currency_amount = shop_currency_amount
        super(shop_room, self).__init__(x, y)

    def show_room_text(self):
        return self.room_text + "\nThis store has {} currency.".format(self.shop_currency_amount)

    def view_shop_inventory(self):
        return "Stock:\n" + '\n'.join('{}'.format(item) for item in self.shop_inventory)

    def buy_item(self, player, item):
        if issubclass(type(item), items.item):
            if item in self.shop_inventory:
                player.inventory.append(item)
                player.currency_amount -= item.value
                self.shop_currency_amount += item.value
                self.shop_inventory.remove(item)
                return "You have bought {} for {} currency.\nYou now have {} currency. The shop now has {} currency.".format(item, item.value, player.currency_amount, self.shop_currency_amount)
            return "The shop does not have {} in store.".format(item)
        return "That is not an item."

    def sell_item(self, player, item):
        if issubclass(type(item), items.item):
            if item in player.inventory:
                self.shop_inventory.append(item)
                self.shop_currency_amount -= item.value
                player.currency_amount += item.value
                player.inventory.remove(item)
                return "You have sold {} for {} currency.\nYou now have {} currency. The shop now has {} currency.".format(item, item.value, player.currency_amount, self.shop_currency_amount)
            return "You have no {} to sell.".format(item)
        return "That is not an item."

class combat_room(loot_room):
    def __init__(self, x, y, room_text_enemy_alive, room_text_enemy_dead, tile_inventory, enemy):
        self.room_text_enemy_dead = room_text_enemy_dead
        self.enemy = enemy
        super(combat_room, self).__init__(x, y, room_text_enemy_alive, tile_inventory)

    def show_room_text(self):
        if self.enemy.is_alive():
            return room_text
        return room_text_enemy_dead

    def enemy_attack(self, player):
        for item in player.inventory:
            if type(item) is items.shield:
                if item.equipped_as_shield:
                    equipped_shield = item
            if type(item) is items.armour:
                if item.equipped_as_armour:
                    equipped_armour = item
        if random.randint(0, 100) >= equipped_shield.block_value:
            player_resistance = 100 - equipped_armour.armour_value
            dealt_damage = int(round((player_resistance * self.enemy.damage) / 100))
            player.hp -= dealt_damage
            if player.is_not_dead():
                return "{} hits you for {} damage!".format(self.enemy, dealt_damage)
            else:
                return "You have fallen as {} has hit you for {} damage!".format(self.enemy, dealt_damage)
        return "{} attacks but misses!".format(self.enemy)