from text_adventure.player import player

class action(object):
    def __init__(self, method, strings):
        self.method = method
        self.strings = strings

    def __str__(self):
        return self.strings[0]

class action_arg(action):
    pass

MoveNorth = action(player.move_north, ["move north", "north"])

MoveSouth = action(player.move_south, ["move south", "south"])

MoveEast = action(player.move_east, ["move east", "east"])

MoveWest = action(player.move_west, ["move west", "west"])

TakeInventory = action(player.take_inventory, ["take inventory", "inventory"])

Attack = action(player.attack, ["attack"])

Equip = action_arg(player.equip, ["equip", "put on"])

Consume = action_arg(player.consume, ["consume", "use"])

Observe = action_arg(player.observe, ["observe", "look at", "stats"])

LookAround = action(player.look_around, ["look around", "search", "stock", "sale", "browse"])

Drop = action_arg(player.drop, ["drop"])

PickUp = action_arg(player.pick_up, ["pick up", "retrieve", "retreive", "take"])

Buy = action_arg(player.buy, ["buy", "purchase"])

Sell = action_arg(player.sell, ["sell"])

Flee = action(player.flee, ["flee", "run away", "retreat"])
