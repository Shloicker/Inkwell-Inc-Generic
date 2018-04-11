import items, enemies, player, random, currency_config

class map_tile(object):
    """A generic map tile - DO NOT create an instance of this class as it only serves as a parent to the classes below. 'x' and 'y' refer to the coordinates of the tile. Note that for the purposes of this game to y axis is inverted (i.e a tile with coordinates (0, 1) is directly below a tile with coordinates (0, 0)). Also note that any rooms that are adjacent to each other can be travelled between by the player."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class starting_room(map_tile):
    """You must create exactly one instance of this class as it will be the player's spawn point. Its coordinates are set to (0, 0) so keep this in mind when building the rest of the map. 'room_text' must be a string - it is the text that will be displayed to the player when they enter the room."""
    def __init__(self, room_text):
        self.room_text = room_text
        super(starting_room, self).__init__(0, 0)

    def show_room_text(self):
        return self.room_text

class loot_room(map_tile):
    """This is a basic room. 'room_text' is as for starting room. 'tile_inventory' must be a list of items (the list can also be empty) that will be found in the room and 'tile_currency_amount' must be an integer that represents the amount of currency found in the room (this can be 0)."""
    def __init__(self, x, y, room_text, tile_inventory, tile_currency_amount):
        self.room_text = room_text
        self.tile_inventory = tile_inventory
        self.tile_currency_amount = tile_currency_amount
        super(loot_room, self).__init__(x, y)

    def show_room_text(self):
        return self.room_text

    def view_tile_inventory(self):
        return '\n'.join('{}'.format(item) for item in self.tile_inventory) + "\nThere is {} {} here.".format(self.tile_currency_amount, currency_config.currency)

    def pick_up_item(self, player, item):
        if item == currency_config.currency:
            picked_up_currency = self.tile_currency_amount
            player.currency_amount += self.tile_currency_amount
            self.tile_currency_amount = 0
            return "You pick up {} {}.".format(picked_up_currency, currency_config.currency)
        if issubclass(type(item), items.item):
            if item in self.tile_inventory:
                player.inventory.append(item)
                self.tile_inventory.remove(item)
                return "You pick up {}.".format(item.name)
            return "There is no {} here.".format(item.name)
        return "That is not an item."

    def drop_item(self, player, item):
        if item == currency_config.currency:
            return "Why would you want to do that??"
        if issubclass(type(item), items.item):
            if item in player.inventory:
                self.tile_inventory.append(item)
                player.inventory.remove(item)
                return "You drop {}".format(item.name)
            return "There is no {} in your inventory.".format(item.name)
        return "That is not an item."

class shop_room(map_tile):
    """A room where the player can buy and sell items. 'room_text' is as for above. 'shop_inventory' is again a list of items that can be empty - this represents the items that are being sold. 'shop_currency_amount' is an integer that represents the currency that the store has available to buy items from the player."""
    def __init__(self, x, y, room_text, shop_inventory, shop_currency_amount):
        self.room_text = room_text
        self.shop_inventory = shop_inventory
        self.shop_currency_amount = shop_currency_amount
        super(shop_room, self).__init__(x, y)

    def show_room_text(self):
        return self.room_text

    def view_shop_inventory(self):
        return "Stock:\n" + '\n'.join('{}'.format(item) for item in self.shop_inventory) + "\nThis store has {} {}.".format(self.shop_currency_amount, currency_config.currency)

    def buy_item(self, player, item):
        if issubclass(type(item), items.item):
            if item in self.shop_inventory:
                player.inventory.append(item)
                player.currency_amount -= item.value
                self.shop_currency_amount += item.value
                self.shop_inventory.remove(item)
                return "You have bought {} for {} {}.\nYou now have {} {}. The shop now has {} {}.".format(item, item.value, currency_config.currency, player.currency_amount, currency_config.currency, self.shop_currency_amount, currency_config.currency)
            return "The shop does not have {} in store.".format(item)
        return "That is not an item."

    def sell_item(self, player, item):
        if issubclass(type(item), items.item):
            if item in player.inventory:
                self.shop_inventory.append(item)
                self.shop_currency_amount -= item.value
                player.currency_amount += item.value
                player.inventory.remove(item)
                return "You have sold {} for {} {}.\nYou now have {} {}. The shop now has {} {}.".format(item, item.value, currency_config.currency, player.currency_amount, currency_config.currency, self.shop_currency_amount, currency_config.currency)
            return "You have no {} to sell.".format(item)
        return "That is not an item."

class combat_room(loot_room):
    """A room in which the player will encounter an enemy. 'room_text_enemy_alive' is as for above with 'room_text' but will only be displayed is the enemy is alive. Similarly 'room_text_enemy_dead' will be displayed if the enemy is dead. 'tile_inventory' is as for loot_room but can only be accessed once the enemy has been killed. Finally 'enemy' must be an enemy."""
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
            if issubclass(type(item), items.shield):
                if item.equipped_as_shield:
                    equipped_shield = item
            if issubclass(type(item), items.armour):
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